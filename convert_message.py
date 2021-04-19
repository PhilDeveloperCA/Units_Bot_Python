from unit import Base_Units, Unit
import copy

async def BasicConvert(message):
    data = message.content
    unit1 = data[data.find('.')+1:data.find('(')]
    unit2 = data[data.find(':')+1:len(data)]
    if(not(unit2 in Base_Units.keys())):
      await message.channel.send(f'{unit2} Invalid Unit, run $convert.show to show the different units that can be used')
      return
    advanced_convert = await AdvancedConvert(message)
    await message.channel.send(advanced_convert)
    return

async def AdvancedConvert(message):
  data = message.content
  unit = []
  unit_strings = []
  operators = []
  numerators = []
  host = data[data.find('(')+1:data.find(')')]
  unit2 = data[data.find(':')+1:len(data)]
  numerators.append(float(host))
  prev_close = data.find(')')
  unit_strings.append(data[data.find('.')+1:data.find('(')])
  unit.append(copy.deepcopy(Base_Units.get(data[data.find('.')+1:data.find('(')])))

  next_mul = data.find('*')
  next_div = data.find('/')
  if(next_mul!=-1 and (next_div>next_mul or next_div == -1)):
    init = data.find('*')
    operators.append('*')
  elif(next_div != -1 and (next_div < next_mul or next_mul == -1)):
    init = data.find('/')
    operators.append('/')
  else:
    init = -1

  while(init > -1):
    unit_strings.append(data[(init+1):data.find('(', prev_close)])
    unit.append(copy.deepcopy(Base_Units.get(data[(init+1):data.find('(', prev_close)])))
    prev_close = data.find(')', prev_close+1)
    host = data[data.find('(', init)+1:data.find(')', init)]
    numerators.append(float(host))
    init = -1
    next_mul = data.find('*', prev_close+1)
    next_div = data.find('/', prev_close+1)
    if(next_mul!=-1 and (next_div>next_mul or next_div == -1)):
      init = data.find('*', prev_close+1)
      operators.append('*')
    elif(next_div!=-1 and (next_div<next_mul or next_mul == -1)):
      init = data.find('/', prev_close+1)
      operators.append('/')
  for us in unit_strings:
     if(not(us in Base_Units.keys())):
        return f'{us} is not a valid unit, to see a list of units, run $convert.show'

  new_unit = Unit.compute(numerators,operators,unit,Base_Units.get(unit2))
  #if(new_unit.startswith('Error')):
  if(isinstance(new_unit,str)):
      return new_unit
  else:
    left_string = f'{numerators[0]}{unit_strings[0]}'
    for i in range(len(operators)):
        left_string += f' {operators[i]} {numerators[i+1]}{unit_strings[i+1]} '
    return f'{left_string} = {new_unit:.3e}{unit2}'

async def TypeConvert(message):
  data = message.content
  units = []
  unit_strings = []
  operators = []
  init = -1
  next_mul = data.find('*')
  next_div = data.find('/')
  if (next_mul != -1 and (next_div > next_mul or next_div == -1)):
    init = data.find('*')
    operators.append('*')
  elif (next_div != -1 and (next_div < next_mul or next_mul == -1)):
    init = data.find('/')
    operators.append('/')

  if(init == -1):
    start_unit = data[data.find(':')+1:len(data)]
    unit_strings.append(start_unit)
    units.append(copy.deepcopy(Base_Units.get(start_unit)))
  else:
    unit_strings.append(data[data.find(':') + 1:init])
    units.append(copy.deepcopy(Base_Units.get(data[data.find(':') + 1:init])))
  while (init > -1):
    prev_init = init
    next_mul = data.find('*', init+1)
    next_div = data.find('/', init+1)
    if (next_mul != -1 and (next_div > next_mul or next_div == -1)):
      init = data.find('*', prev_init+1)
      #init = next_mul
      #operators.append('*', prev_init)
      operators.append('*')
    elif (next_div != -1 and (next_div < next_mul or next_mul == -1)):
      init = data.find('/', prev_init+1)
      #init = next_div
      operators.append('/')
    else:
      init = -1

    if (init == -1):
      start_unit = data[prev_init+ 1:len(data)]
      unit_strings.append(start_unit)
      units.append(copy.deepcopy(Base_Units.get(start_unit)))
    else:
      unit_strings.append(data[prev_init + 1:init])
      units.append(copy.deepcopy(Base_Units.get(data[prev_init + 1:init])))

  for us in unit_strings:
     if(not(us in Base_Units.keys())):
        return f'{us} is not a valid unit, to see a list of units, run $convert.show'
  return Unit.computeType(operators, units)

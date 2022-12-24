import random
import os
import string
import sys

print(sys.setrecursionlimit(10000))
print("Limit is : ", sys.getrecursionlimit())

def generate_random_string(length=1):
    Rndmha = ['x','a','b','y','z','c']
#  return ''.join(random.choices(string.ascii_letters, k=length))
    return ''.join(random.choices(Rndmha, k=length))


# Generate a random JavaScript function
def generate_random_js_function():
  function_args =[
    f'eval({generate_random_string()});;',
    f'Function({generate_random_string()});',
    f'new Function({generate_random_string()});',
    f'Object.assign({generate_random_string()},{generate_random_string()});'f'Object.create({generate_random_string()});',
    f'Function({generate_random_string()});',
    f'new Function({generate_random_string()});',
    f'Object.assign({generate_random_string()}, {generate_random_string()});',
    f'Object.create({generate_random_string()});',
    f'Object.freeze({generate_random_string()});',
    f'Object.getOwnPropertyDescriptor({generate_random_string()}, {generate_random_string()});',
    f'Object.getOwnPropertyDescriptors({generate_random_string()});',
    f'Object.getOwnPropertyNames({generate_random_string()});',
    f'Object.getOwnPropertySymbols({generate_random_string()});',
    f'Object.is({generate_random_string()}, {generate_random_string()});',
        #---------------------------------------------------------------------#
    f'Function({generate_random_string()});',
    f'new Function({generate_random_string()});',
    f'Object.assign({generate_random_string()},{generate_random_string()});',
    f'Object.create({generate_random_string()});',
    f'Object.freeze({generate_random_string()});',
    f'Object.getOwnPropertyDescriptor({generate_random_string()},{generate_random_string()});',
    f'Object.getOwnPropertyDescriptors({generate_random_string()});'
    f'Object.getOwnPropertyNames({generate_random_string()});'
    f'Object.getOwnPropertySymbols({generate_random_string()});',
    #---------------------------------------------------------------------#
    f'Object.isExtensible({generate_random_string()});',
    f'Object.isFrozen({generate_random_string()});',
    f'Object.isSealed({generate_random_string()});',
    f'Object.keys({generate_random_string()});',
    f'Object.preventExtensions({generate_random_string()});',
    f'Object.seal({generate_random_string()});',
    f'Object.setPrototypeOf({generate_random_string()}, {generate_random_string()});',
    f'Object.values({generate_random_string()});'
    
  ]
  return random.choice(function_args) 
  

# Generate a random JavaScript function
def generate_random_js_functions(js_funcs):
  function_name = generate_random_string()
  function_args = ', '.join([generate_random_string() for _ in range(random.randint(0, 3))])
  function_body = '\n'.join([js_funcs for _ in range(random.randint(1, 5))])
  return f'function {function_name}({function_args}) {{\n{function_body}\n}}'
  

def generate_random_js_expression():
  expressions = [
    generate_random_string(),
    f'{generate_random_string()} + {generate_random_string()};',
    f'{generate_random_string()} - {generate_random_string()};',
    f'{generate_random_string()} * {generate_random_string()};',
    f'{generate_random_string()} / {generate_random_string()};',
    f'{generate_random_string()} % {generate_random_string()};',
    f'{generate_random_string()} ** {generate_random_string()};',
    f'{generate_random_string()} == {generate_random_string()};',
    f'{generate_random_string()} != {generate_random_string()};',
    f'{generate_random_string()} === {generate_random_string()};',
    f'{generate_random_string()} !== {generate_random_string()};',
    f'{generate_random_string()} > {generate_random_string()};',
    f'{generate_random_string()} >= {generate_random_string()};',
    f'{generate_random_string()} < {generate_random_string()};',
    f'{generate_random_string()} <= {generate_random_string()};',
    f'{generate_random_string()} && {generate_random_string()};',
    f'{generate_random_string()} || {generate_random_string()};',
    f'{generate_random_string()} !{generate_random_string()};',
    f'typeof {generate_random_string()};',
    f'void {generate_random_string()};',
    f'{generate_random_string()}[{generate_random_string()}]',
    f'{generate_random_string()}.{generate_random_string()};',
    f'{generate_random_string()}({generate_random_string()};',
    f'new {generate_random_string()}({generate_random_string()};'
  ]
  return random.choice(expressions)

defs = """var x = 10;
var a = [1, 2, 3];
var b = null;
var c = undefined;
var y = "test";
var z = {a: 1, b: 2};"""


# List of valid JavaScript statements
statements = [
    'console.log("Hello, world!");',
    'var x = 10;',
    'x += 5;',
    'if (x > 15) { console.log("x is greater than 15"); }',
    'function add(a, b) { return a + b; }',
    'console.log(add(x, 5));',
    'var y = "test";',
    'y = y.substring(1);',
    'y = y.toUpperCase();',
    'console.log(y);',
    'for (var i = 0; i < 10; i++) { console.log(i); }',
    'var z = {a: 1, b: 2};',
    'console.log(z.a);',
    'console.log(z["b"]);',
    'var a = [1, 2, 3];',
    'console.log(a[0]);',
    'console.log(a.length);',
    'try { throw "error"; } catch (e) { console.log(e); }',
    'var b = null;',
    'console.log(b);',
    'var c = undefined;',
    'console.log(c);',
    'console.log("Hello, world!");',
    'var x = 10;',
    'x += 5;',
    'if (x > 15) { console.log("x is greater than 15"); }',
    'function add(a, b) { return a + b; }',
    'console.log(add(x, 5));',
    'var y = "test";',
    'y = y.substring(1);',
    'y = y.toUpperCase();',
    'console.log(y);',
    'for (var i = 0; i < 10; i++) { console.log(i); }',
    'var z = {a: 1, b: 2};',
    'console.log(z.a);',
    'console.log(z["b"]);',
    'var a = [1, 2, 3];',
    'console.log(a[0]);',
    'console.log(a.length);',
    'try { throw "error"; } catch (e) { console.log(e); }',
    'var b = null;',
    'console.log(b);',
    'var c = undefined;',
    'console.log(c);',
    f'{generate_random_string()} * {generate_random_string()};',
    f'{generate_random_string()} / {generate_random_string()};',
    f'{generate_random_string()} % {generate_random_string()};',
    f'{generate_random_string()} ** {generate_random_string()};',
    f'{generate_random_string()} == {generate_random_string()};',
    f'{generate_random_string()} != {generate_random_string()};',
    f'{generate_random_string()} === {generate_random_string()};',
    f'{generate_random_string()} <= {generate_random_string()};',
    f'{generate_random_string()} && {generate_random_string()};',
    f'{generate_random_string()} || {generate_random_string()};',
        ]

# Set the number of files to generate
num_files = 200

# Generate the files
for i in range(num_files):
    
    # Generate a random number of statements
    num_statements = random.randint(1, 45)

    # Choose a random subset of the statements
    chosen_statements = random.sample(statements, num_statements)

    # Concatenate the statements into a single string
    js_code = '\n'.join(chosen_statements)
    js_funcs = '\n'.join(chosen_statements)
    
    Fnko = generate_random_js_function()
    
    Fnks = generate_random_js_functions(js_funcs)
    
    Exp = generate_random_js_expression()

    # Generate a random number of newlines and spaces
    newlines = '\n' * random.randint(0, 10)
    spaces = ' ' * random.randint(0, 10)

    # Insert the newlines and spaces randomly into the code
    #js_code = newlines + js_code + spaces + newlines + generate_random_js_expression()
    #js_code = defs + newlines + 'try {'+ Fnks +'} catch (e)'+'{ console.log(e); }'+ js_code + spaces + 'try {'+ Fnko +' } catch (e)'+'{ console.log(e); }'+ newlines + 'try {'+ Exp +' } catch (e)'+'{ console.log(e); }'
    js_code = defs + newlines + 'try {'+ Fnks +'} catch (e)'+'{ console.log(e); }'+ 'try {'+ js_code +'} catch (e)'+'{ console.log(e); }' + spaces + 'try {'+ Fnko +' } catch (e)'+'{ console.log(e); }'+ newlines + 'try {'+ Exp +' } catch (e)'+'{ console.log(e); }'

    # Write the code to a file
    with open(f'random_{i}.js', 'w') as f:
        f.write(js_code)
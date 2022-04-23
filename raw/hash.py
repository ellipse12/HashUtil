import sys
import typer
import os
import hashlib
path = os.path.dirname(os.path.abspath(__file__))



 



 
def hash(data, algorithm, length): #takes a hash algorithm and outputs the hash of the input with that algorithm
	data = str(data).encode('utf-8')
	match algorithm.lower():
		case 'sha256': #id: 0
			sha3_512 = hashlib.sha256(data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case '':#id:0
			sha3_512 = hashlib.sha256(data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'md5':#id:1
			sha3_512 = hashlib.md5(data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'mdc2':#id:2
			sha3_512 = hashlib.new('mdc2',data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'md5-sha1':#id:3
			sha3_512 = hashlib.new('md5-sha1',data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'sha1':#id:4
			sha3_512 = hashlib.sha1(data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'sha224':#id:5
			sha3_512 = hashlib.sha224(data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'md4':#id:6
			sha3_512 = hashlib.new('md4',data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'sha384':#id:7
			sha3_512 = hashlib.sha384(data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'sha512':#id:8
			sha3_512 = hashlib.sha512(data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'sha512_224':#id:9
			sha3_512 = hashlib.new('sha512_224',data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest
				
		case 'sha512_256':#id:10
			sha3_512 = hashlib.new('sha512_256',data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'sha3_224':#id:11
			sha3_512 = hashlib.sha3_224(data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'sha3_256':#id:12
			sha3_512 = hashlib.sha3_256(data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'sha3_384':#id:13
			sha3_512 = hashlib.sha3_384(data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'sha3_512':#id:14
			sha3_512 = hashlib.sha3_512(data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'shake128':#id:15
			sha3_512 = hashlib.shake_128(data)
			sha3_512_hex_digest = sha3_512.hexdigest(length)
			return sha3_512_hex_digest

		case 'shake256':#id:16
			sha3_512 = hashlib.shake_256(data)
			sha3_512_hex_digest = sha3_512.hexdigest(length)
			return sha3_512_hex_digest

		case 'blake2b':#id:17
			sha3_512 = hashlib.blake2b(data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'blake2s':#id:18
			sha3_512 = hashlib.blake2s(data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'whirlpool':#id:19
			sha3_512 = hashlib.new('whirlpool',data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'sm3':#id:20
			sha3_512 = hashlib.new('sm3',data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest

		case 'ripemd160':#id:21
			sha3_512 = hashlib.new('ripemd160',data)
			sha3_512_hex_digest = sha3_512.hexdigest()
			return sha3_512_hex_digest


def helper(algorithmx): #finds the appropriate help menu
	global algorithms
	global ids
	global path
	if str(algorithmx) in ids:
		with open(path + '/help/algorithms/' + str(algorithms[int(algorithmx)])+'.txt','r') as w:
			print(w.read())
	elif str(algorithmx) in algorithms:
		with open(path + '/help/algorithms/' + str(algorithmx)+'.txt','r') as w:
			print(w.read())
	else:
		typer.echo(f"""Algorithm Id: {str(algorithmx).upper()} Is Not Supported! Please Use "hash --help" For a List of Supported Algorithms.""", err = True)
		raise typer.Exit()

#list of all the supported algorithms	
algorithms = ['sha256','md5','mdc2','md5-sha1','sha1','sha224','md4','sha384','sha512','sha512_224','sha512_256','sha3_224','sha3_256','sha3_384','sha3_512','shake128','shake256','blake2b','blake2s'
, 'whirlpool','sm3','ripemd160','']


#list of all the algorithm ids
ids = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']




def hasher(input, algorithm, length):
	global algorithms
	global ids

	if algorithm in algorithms:
		typer.echo(hash(input, algorithm, length))
	elif algorithm in ids:
		typer.echo(hash(input, algorithms[int(algorithm)], length))
	else:
		typer.echo(f"""Algorithm Id: {algorithm} Is Not Supported! Please Use "hash --help" For a List of Supported Algorithms.""", err = True)
		raise typer.Exit()



def main(input: str = typer.Argument('', show_default = False), algorithmid: str = typer.Argument('0'), length: int = typer.Argument(32),help: bool = typer.Option(False, '--help',show_default=False),helps: str = typer.Option(None,'-?',show_default=False), file: str = typer.Option(None, '-f', show_default = False)):
    global path
    if help:
    	with open(path + '/help/help.txt','r') as hel:
    		typer.echo(hel.read())
    	raise typer.Exit()

    if helps:
    	helper(str(helps))
    	raise typer.Exit()

    if file:
    	info = ""
    	try:
    		with open(str(file),'r') as files:
    			info = files.read()
    	except FileNotFoundError:
    		typer.echo(f"""FileNotFoundError: No such file or directory: '{str(file)}'""")
    		raise typer.Exit()

    	hasher(str(info), str(algorithmid).lower(), int(length))

    	raise typer.Exit()

    hasher(str(input), str(algorithmid).lower(), int(length))
    




if __name__ == "__main__":
    typer.run(main)




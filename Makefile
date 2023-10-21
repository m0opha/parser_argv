parser_test:
	@python3 ./src/Parser.py 1 2 3 4 --host 192.168.1.1 --user m0opha --password 1234 --path /home/m0opha/Documents -a 123 -b abc -d ?¡? -hola javier

add_argv_test: 
	@python ./src/add_argv.py


.PHONY: argv_test
.PHONY: add_argv_test


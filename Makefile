.PHONY: clean, pull, push, reqs, update
clean:
	rm -rf *.pyc
pull:
	git pull origin master
push:
	git push origin master
	git push github master
update: pull push
reqs:
	pip freeze > requirements.txt

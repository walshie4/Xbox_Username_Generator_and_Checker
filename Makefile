.PHONY: clean, pull, push, reqs, update, run, test
clean:
	rm -rf wsgi/*.pyc
pull:
	git pull origin master
push:
	git push origin master
	git push github master
update: pull push
reqs:
	pip freeze > requirements.txt
run: test
test:
	python wsgi/xboxutil.py


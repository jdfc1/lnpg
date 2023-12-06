TAG=$(shell date +%d.%m.%Y)

add:	
	git add .
commit: add
	git commit -m " -> Enviado no dia $(TAG) para o repositório online."
push: 	commit
	git push
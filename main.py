#TERMINEI: 14/04/2022
# COPIEI DO TODO NO DB DO PROF EDUARDO (ednascimento) e deu certo finalmente! 

# Você foi encarregado de criar um sistema de agenda de contatos. Primeiramente crie uma variavel chamada contacts para armazenar os contatos da agenda

#Logo após, crie a rota principal (/) com a frase Agenda de Contatos em h1, que mostre uma lista de contatos cadastrados para serem editados e deletados e tenha um fomulário com três inputs de nomes name, email e phone. Faça as rotas (/create) que recebe os dados do formulário via POST e cadastre um contato, (/delete) que deleta um contato específico e (/update) que edita um contato específico. Utilize a imagem a seguir como referência.


from flask import Flask, render_template, request, redirect
app = Flask('app')

contacts = []

@app.route('/')
def index():
  return render_template(
    'index.html',
    contacts=contacts
  )

@app.route('/create', methods=['POST'])
def create():
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  contacts.append({
    'name': name,
    'email': email,
    'phone': phone,
  })
  return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
  contacts.pop(index)
  return redirect('/')

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
  name = request.form.get('name')
  email = request.form.get('email')  
  phone = request.form.get('phone')
  contacts[index]['name'] = name
  contacts[index]['email'] = email
  contacts[index]['phone'] = phone
  return redirect('/')

# IMPORTANTE 
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
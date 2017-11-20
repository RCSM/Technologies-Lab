const express = require('express');
const mongodb = require('mongodb');
require('dotenv').config(); // Checar se essa linha é necessária
//const uri = process.env.URI; --> Corrigir a URI para um arquivo externo
const uri = "mongodb://mdbTrial:MdbTrialP455WD@ds255715.mlab.com:55715/mongodbtrial"
const app = express();
app.use(require('cors')()); // Permite requisições CORS(cross domain resource sharing)
app.use(require('body-parser').json()) // Transforma dados de requisições automaticamente em JSON

mongodb.MongoClient.connect(uri, function(err, db) {

	const collection = db.collection('users');

	app.get("/", function (req, res) {
		res.send("Hey, someone connected via GET HTTP method :D");
	});

	app.get("/:user", function (req, res) {
		console.log("User " + req.params.user + " just logged in...");
		res.send("User " + req.params.user + "logged successfully!");
	});

	// Pega dados de um usuário
	app.get("/:user", function(req, res) {
		collection.find({ user : req.params.user }).toArray(function (err, docs) {
			if (err) {
				res.send("Usuario nao encontrado =x");
			} else {
				res.send(docs);
			}
		});
	});

	// Atualiza dados do usuário
	app.post("/:user", function (req, res) {
		collection.updateOne({ user : req.params.user }, 
			{$set:{ ...req.body, user : req.params.user}},
			function (err, r) {
				if (err) {
					res.send("A atualizacao dos dados falhou x.x'");
				} else {
					res.send("Dados atualizados com sucesso!");
				}
		});
	});

	// Cria um documento para um novo usuário
	app.post("/:user", function(req, res) {
		collection.insertOne({ ...req.body, user : req.params.user }, function(err, r) {
			if (err) {
				res.send("Um erro ocorreu e o documento nao foi criado :(");
			} else {
				res.sen("O documento para o usuario " + req.params.user + " criado!");
			}
		})
	});

	var listener = app.listen(process.env.PORT, function() {
		console.log('Servidor rondando na porta ' + listener.address().port);
	});
});
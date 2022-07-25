import re
from flask import Flask, jsonify, request
from http import HTTPStatus

#CRUD

app=Flask(__name__)

recetas = [{"id":1,
            "nombre":"ensalada rusa",
            "descripcion": "encantadora receta de ..."},
            {"id":2,
            "nombre":"paella",
            "descripcion": "receta de paella..."}]

# get all
@app.route('/recetas/', methods=['GET'])
def obtener_recetas():
    return jsonify({'datos': recetas})

# get 1
@app.route('/recetas/<int:receta_id>', methods=['GET'])
def obtener_receta(receta_id):
    for receta in recetas:
        if receta['id']==receta_id:
            return jsonify(receta)
    return jsonify({'message':"receta no encontrada"})

# crear receta
@app.route('/recetas', methods=['POST'])
def crear_receta():
    data= request.get_json()
    nombre= data.get('nombre')
    descripcion= data.get('descripcion')
    receta = {
        'id': len(recetas)+1,
        'nombre': nombre,
        'descripcion': descripcion}
    recetas.append(receta)
    return jsonify({'message':"receta insertada correctamente"}), HTTPStatus.CREATED


# update
@app.route('/recetas/<int:receta_id>', methods=['PUT'])
def actualizar_receta(receta_id):
    bandera=False
    for receta in recetas:
        print (type(receta), receta)
        id_r = receta['id']
        if id_r == receta_id:
            print("actualizar")
            bandera=True
            data = request.get_json()
            receta.update(
                {
                    'nombre':data.get("nombre"),
                    'descripcion':data.get("descripcion")
                }
            )
            return jsonify({'message':"receta actualizada correctamente"}), HTTPStatus.OK
    if not bandera:
        return jsonify({'message': "receta no encontrada"})


# delete
@app.route('/recetas/<int:receta_id>', methods=['DELETE'])
def eliminar_receta(receta_id):
    bandera=False
    for receta in recetas:
        id_r = receta['id']
        if id_r == receta_id:
            bandera=True
            recetas.remove(receta)
            return jsonify({'message':"receta eliminada correctamente"}), HTTPStatus.OK
    if not bandera:
        return jsonify({'message': "receta no encontrada"})



app.run(host='0.0.0.0', port=5000)
#app.run()
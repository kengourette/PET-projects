import catboost as cb
import pandas as pd


from flask import Flask, jsonify, request

# Загрузка модели
model = cb.CatBoostClassifier()
model.load_model("final_model.cbm")

# Инициализация приложения
app = Flask("default")


# Настройка конечной точки для предсказания
@app.route("/predict", methods=["POST"])
def predict():
    # Получение предоставленного JSON
    X = request.get_json()
    # Выполнение предсказания
    preds = model.predict(pd.DataFrame(X, index=[0]))[0][0]



    # Вывод JSON с предсказанием класса
    result = {"predict for class": preds}
    return jsonify(result)


if __name__ == "__main__":
    # Run the app on local host and port 8989
    app.run(debug=True, host="0.0.0.0", port=8989)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

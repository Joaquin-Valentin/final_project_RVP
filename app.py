from flask import Flask, render_template, url_for, request
import pickle
import os
import numpy as np

app = Flask(__name__, template_folder='C:/Users/Usuario/demo/Ironhack/Final_Project/templates')#templates
app.config['UPLOAD_FOLDER'] = os.getcwd()
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#load the pickled model
with open('/Users/Usuario/demo/Ironhack/Final_Project/model.p', 'rb') as file:
    model = pickle.load(file)

#define dictionaries

price_dict= {'Medium': [4.2],
              'Low': [4.1],
                'High': [4.3],
                  'Expensive': [4.5]}

district_dict = {'HORTALEZA': [37.68844221105528,
  17.86317948717949,
  200.0174358974359,
  0.0265333333333333,
  0.4170234232804233],
 'SAN BLAS-CANILLEJAS': [62.264150943396224,
  10.819877344877344,
  114.56204906204906,
  0.016060606060606,
  0.429501996124031],
 'RETIRO': [124.35424354243544,
  26.43293768545994,
  174.58753709198814,
  0.0080415430267062,
  0.5387095089285714],
 'SALAMANCA': [110.26119402985074,
  31.00871404399324,
  246.12013536379013,
  0.0090693739424703,
  0.5533441939393939],
 'CIUDAD LINEAL': [126.90972222222224,
  15.225889192886456,
  146.30984952120383,
  0.0078796169630642,
  0.45997566877303847],
 'MORATALAZ': [115.46052631578948,
  16.511823361823364,
  131.6096866096866,
  0.0086609686609686,
  0.3986984492753623],
 'VICALVARO': [12.55656108597285,
  17.23536036036036,
  178.66666666666666,
  0.0796396396396396,
  0.3828384523809524],
 'FUENCARRAL-EL PARDO': [1.7058823529411764,
  57.57610837438424,
  606.6034482758621,
  0.5862068965517241,
  0.4412468543046358],
 'CHAMARTIN': [61.62280701754386,
  34.84804270462634,
  256.88790035587186,
  0.0162277580071174,
  0.5511867705382436],
 'TETUAN': [109.12476722532588,
  19.5872866894198,
  268.65699658703073,
  0.0091638225255972,
  0.47567358304297325],
 'VILLA DE VALLECAS': [5.65158283161779,
  17.846391752577322,
  394.5601374570447,
  0.1769415807560137,
  0.4064768031189083],
 'PUENTE DE VALLECAS': [46.09164420485176,
  12.099049707602338,
  344.5,
  0.0216959064327485,
  0.41296009895833335],
 'CHAMBERI': [138.0549682875264,
  25.72970903522205,
  210.24042879019908,
  0.0072434915773353,
  0.5590027025641026],
 'CENTRO': [114.3953934740883,
  19.33414429530201,
  234.3657718120805,
  0.008741610738255,
  0.6483508805668016],
 'USERA': [93.63636363636364,
  13.861026352288487,
  195.2954230235784,
  0.0106796116504854,
  0.3891695854483926],
 'ARGANZUELA': [151.840490797546,
  16.135050505050504,
  154.17979797979797,
  0.0065858585858585,
  0.5025478828828829],
 'CARABANCHEL': [47.02127659574468,
  16.223378582202113,
  385.3906485671192,
  0.0212669683257918,
  0.41269010939510936],
 'LATINA': [14.998036906164115,
  30.92473821989529,
  620.5445026178011,
  0.066675392670157,
  0.41832607007575756],
 'MONCLOA-ARAVACA': [7.531740908112761,
  29.571285714285715,
  343.8857142857143,
  0.1327714285714285,
  0.5085112244897959],
 'VILLAVERDE': [23.701138050470064,
  15.207933194154489,
  321.1461377870564,
  0.0421920668058455,
  0.33642315873015877]}
zip_code_dict = {'28050': [8.05851723282916, 
                           531.0],
 '28042': [18.125268125268125, 
           211.0],
 '28022': [3.903903903903904, 
           278.5],
 '28037': [4.436254436254436, 
           184.0],
 '28009': [37.954621287954616, 
           593.0],
 '28007': [22.33165368758589, 
           359.0],
 '28001': [127.62762762762762, 
           858.0],
 '28028': [20.7025207025207, 
           273.5],
 '28006': [45.48237557946296, 
           731.0],
 '28027': [13.61826943222292,
           235.5],
 '28017': [4.03852127990059, 
           134.5],
 '28043': [2.723653886444584, 
           264.5],
 '28033': [7.773259985649367, 
           273.0],
 '28030': [5.005005005005005, 
           232.0],
 '28032': [6.142506142506143, 
           237.0],
 '28052': [46.85766005248785, 
           355.0],
 '28034': [9.00900900900901, 
           283.0],
 '28049': [18.29954954954955, 
           546.0],
 '28048': [585.5855855855856, 
           769.0],
 '28035': [5.323505323505324, 
           327.5],
 '28016': [10.71193144363876, 
            514.0],
 '28036': [33.78378378378379, 
            775.0],
 '28046': [80.90327169274538, 
            538.0],
 '28002': [21.5994683207798, 
            474.5],
 '28020': [16.52862539959314, 
            688.5],
 '28029': [17.6381200477586, 
            267.5],
 '28039': [46.85766005248785, 
            142.0],
 '28031': [17.66853059956508, 
            215.5],
 '28051': [4.962589708352421, 
            627.0],
 '28053': [6.506506506506507, 
            82.5],
 '28038': [4.436254436254436, 
            107.0],
 '28018': [10.647010647010648, 
            143.0],
 '28010': [100.46811517399752, 
            542.0],
 '28003': [65.06506506506507, 
            653.0],
 '28015': [85.3018372703412, 
            578.5],
 '28004': [243.993993993994, 
            1220.5],
 '28012': [254.7297297297297, 
            1294.0],
 '28005': [151.27627627627626, 
            729.0],
 '28014': [295.94110239271527, 
            836.0],
 '28013': [259.4366518417152, 
            1843.0],
 '28026': [9.679100588191496, 
            174.0],
 '28041': [3.706237883453073, 
            147.0],
 '28045': [72.22222222222221, 
            380.0],
 '28019': [33.599172943435235, 
            109.5],
 '28025': [12.84178915757863, 
            125.0],
 '28047': [33.78378378378379, 
            451.0],
 '28044': [6.80913471611146, 
            357.0],
 '28054': [64.04842342342342, 
            563.5],
 '28024': [20.913770913770914, 
           761.0],
 '28011': [56.66957279860506, 
           159.0],
 '28008': [86.64276521419379, 
           500.0],
 '28021': [8.209143723162414, 
           116.0]}

@app.route('/')

def home():
    return render_template('index.html', css_url = url_for('static', filename='css/styles.css'), js_url = url_for('static', filename='js/scripts.js'))

@app.route('/', methods=['POST'])

@app.route('/predict', methods=['GET','POST'])

def predict():
    
    # Get user input from the form
    zip_codes = sorted(zip_code_dict.keys())
    districts = sorted(district_dict.keys())
    price_levels = sorted(price_dict.keys())

    if request.method == "GET":
        return render_template("predict.html", zip_codes=zip_codes, districts=districts, price_levels=price_levels)
    elif request.method == "POST":
        zip_code = request.form["zip_code"]
        district = request.form["district"]
        website = int(request.form["website"])
        delivery = int(request.form["delivery"])
        veggie_food = int(request.form["veggie_food"])
        serves_alcohol = int(request.form["serves_alcohol"])
        reservable = int(request.form["reservable"])
        dine_in = int(request.form["dine_in"])
        takeout = int(request.form["takeout"])
        price_level = request.form["price_level"]
        
        # Assign values from dictionaries for zip code, district, and price level
        zip_code_value = zip_code_dict.get(zip_code)
        print(zip_code_value)
        '''if zip_code_value is None:
            # Handle case where zip_code is not found in dictionary
            zip_code_value = [0, 0]'''
        district_value = district_dict.get(district)
        print(district_value)
        '''if district_value is None:
            # Handle case where district is not found in dictionary
            district_value = [0] * 5'''
        print(price_dict.items())
        price_value = price_dict.get(price_level)
        print(price_value)
        print(f"price_dict: {price_dict}")
        print(f"price_level: {price_level}")
        print(f"price_value: {price_value}")
        if price_value is None:
            # Handle case where price_level is not found in dictionary
            price_value = [4.275]

        # Convert the lists to numpy arrays
        district_value = np.array(district_value)
        zip_code_value = np.array(zip_code_value)
        price_value = np.array(price_value)
        delivery = np.array([delivery])
        dine_in = np.array([dine_in])
        reservable = np.array([reservable])
        veggie_food = np.array([veggie_food])
        takeout = np.array([takeout])
        website = np.array([website])
        serves_alcohol = np.array([serves_alcohol])

        # Combine the input values into a single array
        values_list = []
        values_list.extend(district_value)
        values_list.extend(zip_code_value)
        values_list.extend(price_value)
        values_list.extend([delivery, dine_in, reservable, veggie_food, takeout, website, serves_alcohol])

        # Reshape the array to have shape (1, 15)
        inputs = np.array(values_list).reshape((1, 15))

        prediction = model.predict(inputs)

        # Return the prediction to the user
        return render_template("predict.html", prediction=prediction, zip_codes=zip_codes, districts=districts, price_levels=price_levels)
    
if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')
from flask import Flask, render_template, request
from scripts.controllers import *

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/get_file', methods=['POST'])
def generate_file_with_groups():

    group_names = []
    file = request.files['file']
    result = return_excel_file_data(file)

    for each in result['Additional comments'].tolist():
        for ele in extract_group_names(each):
            group_names.append(ele)
    
    group_count = get_group_count(group_names)
    
    # output_file = open("output_file.txt", "w")
    # for each_group in group_count:
    #     output_file.write(each_group, )
    with open("output_file.txt", 'w') as file:
        for key, value in group_count.items():
            file.write(f"{key}: {value}\n")
    
    return "success"
    
    
if __name__ == '__main__':
    app.run()
from flask import Flask, request, jsonify

app = Flask(__name__)

def reverse_engineer(inputs):
    cyclic_pattern = [3, 4, 2] 
    outputs = []  

    for idx, input_array in enumerate(inputs):
        if idx == 0:
            next_array = inputs[idx + 1]
            outputs.append([x + y for x, y in zip(input_array, next_array)])
        elif idx == 1:
            outputs.append([x + cyclic_pattern[i % len(cyclic_pattern)] for i, x in enumerate(input_array)])
        elif idx == 2:
            decremented_previous = [y - (1 if i == len(input_array) - 1 else 0) for i, y in enumerate(inputs[idx - 1])]
            outputs.append([x + y for x, y in zip(input_array, decremented_previous)])
        else:
            outputs.append([x + cyclic_pattern[i % len(cyclic_pattern)] for i, x in enumerate(input_array)])
    
    return outputs

@app.route('/reverse_engineer', methods=['POST'])
def reverse_engineer_api():
    try:

        data = request.get_json()
        inputs = data.get('inputs', [])
        

        if not inputs or not all(isinstance(arr, list) for arr in inputs):
            return jsonify({'error': 'Invalid input. Please provide a list of lists.'}), 400
        

        outputs = reverse_engineer(inputs)
        return jsonify({'outputs': outputs})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

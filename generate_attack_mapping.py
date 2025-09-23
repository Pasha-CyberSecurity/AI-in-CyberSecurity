import openai

def set_api_key(api_key):
    openai.api_key = api_key

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def generate_response(input_text, context_text, selected_model):
    messages = [
        {"role": "system", "content": context_text},
        {"role": "user", "content": input_text}
    ]
    response = openai.ChatCompletion.create(
        model=selected_model,
        messages=messages
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    # Step 1: Set your OpenAI API key
    api_key = "YOUR_OPENAI_API_KEY"
    set_api_key(api_key)
    
    # Step 2: Read context instructions from Context.txt
    context_text = read_file("Context.txt")
    
    # Step 3: Read user input query from CVE-dataset.txt
    input_text = read_file("CVE-dataset.txt")
    
    # Step 4: Specify your desired OpenAI model
    selected_model = "gpt-4"  # or any other model you want
    
    # Step 5: Generate mapped ATT&CK techniques
    mapped_techniques = generate_response(input_text, context_text, selected_model)
    
    # Output the result
    print("Generated mapped ATT&CK Techniques:\n")
    print(mapped_techniques)

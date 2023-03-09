'''curl https://dufs.budgetapp.works/ -F file=@temp_0000.wav'''


url_ = 'https://dufs.budgetapp.works/'
    # Open the file and read its contents
    with open('temp_0000.wav', 'rb') as f:
        file_content = f.read()

    # Define the data to be uploaded
    data = {'upload_file': file_content}

    # Upload the file to the server
    response = requests.post(url_, files=data)

    # Check the response status code
    if response.status_code == 200:
        print('File uploaded successfully')
    else:
        print(f'Error uploading file: {response.status_code}')


'''files = {'file': open(autospeech_filename, 'rb')}
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, files=files, headers=headers)'''

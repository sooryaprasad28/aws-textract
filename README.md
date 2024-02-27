# Extract Text from Documents with AWS Textract

This project aims to extract text from documents using AWS Textract, providing a convenient graphical user interface (GUI) for users to upload documents and view the extracted text.

# Features
- Upload documents (currently supports JPG format) using a GUI interface.
- Utilize AWS Textract service to extract text from uploaded documents.
- View extracted text in the application's interface.
- Supports uploading multiple documents for text extraction.

# Technologies Used
- **Python**: Used as the primary programming language.
- **Tkinter**: Python library for creating GUI applications.    
- **PIL (Python Imaging Library)**: Library for image processing, used for image resizing and display.
- **boto3**: AWS SDK for Python, used for interacting with AWS services such as Textract.
- **AWS Textract**: AWS service for extracting text from documents.
- **AWS IAM**: AWS Identity and Access Management for managing access to AWS services securely.

# Setup
1. Clone the repository:

    git clone https://github.com/sooryaprasad28/aws-textract/

2. Install dependencies:

    pip install boto3 pillow awscli

3. Create an IAM user for AWS Textract:
    - Go to the [IAM console](https://console.aws.amazon.com/iam/).
    - Click on "Users" in the navigation pane.
    - Click on "Add user" and follow the prompts to create a new IAM user.
    - Make sure to grant the necessary permissions to the IAM user, such as AmazonTextractFullAccess.
    - Take note of the IAM user's Access Key ID and Secret Access Key, which you'll use to configure AWS CLI.

4. Configure AWS credentials:
    - If you haven't already configured AWS CLI, you can do so by running command: **aws configure**
    - Follow the prompts to input your AWS Access Key ID, AWS Secret Access Key, region, and output format.
    - Ensure AWS credentials are properly configured on your system, can be manually set up AWS credentials using the AWS CLI or AWS Management Console.

# Usage
1. Run the application: **python textract.py**
2. Upload a document for text extraction by clicking on "Select Document for Text Extraction" button.
3. Click on "Display Text" to view the extracted text from the document.
4. To upload another document, click on "Upload Another File".

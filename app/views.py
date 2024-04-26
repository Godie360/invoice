import re
import pytesseract
from PIL import Image
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Invoice


@login_required
def extract_data(request, invoice_id):
    invoice = Invoice.objects.get(pk=invoice_id)
    text = pytesseract.image_to_string(Image.open(invoice.invoice_file))

    # Initialize variables to store extracted data
    school_name = "Not found"
    invoice_amount = "Not found"
    parent_name = "Not found"
    account_number = "Not found"

    # Search for patterns in the text and extract data
    school_name_match = re.search(r'School Name: (.+)', text)
    invoice_amount_match = re.search(r'Invoice Amount: (.+)', text)
    parent_name_match = re.search(r'Parent Name: (.+)', text)
    account_number_match = re.search(r'Account Number: (.+)', text)

    # Check if matches are found and extract data if available
    if school_name_match:
        school_name = school_name_match.group(1)
    if invoice_amount_match:
        invoice_amount = invoice_amount_match.group(1)
    if parent_name_match:
        parent_name = parent_name_match.group(1)
    if account_number_match:
        account_number = account_number_match.group(1)

    return render(request, 'app/invoice_details.html', {
        'school_name': school_name,
        'invoice_amount': invoice_amount,
        'parent_name': parent_name,
        'account_number': account_number
    })

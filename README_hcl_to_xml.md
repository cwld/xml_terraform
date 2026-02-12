# HCL to XML Converter

Converts Terraform HCL configuration files to XML format.

## Installation

```bash
pip install python-hcl2
```

## Usage

```bash
python3 hcl_to_xml.py <terraform_file.tf>
```

## Example

Input (`example.tf`):
```hcl
resource "aws_instance" "example" {
  ami           = "ami-123456"
  instance_type = "t2.micro"
}

output "instance_id" {
  value = aws_instance.example.id
}
```

Output:
```xml
<?xml version="1.0" ?>
<terraform>
  <resource>
    <aws_instance>
      <example>
        <ami>ami-123456</ami>
        <instance_type>t2.micro</instance_type>
      </example>
    </aws_instance>
  </resource>
  <output>
    <instance_id>
      <value>aws_instance.example.id</value>
    </instance_id>
  </output>
</terraform>
```

## Features

- Parses any valid Terraform HCL file
- Preserves structure of resources, variables, outputs, and other blocks
- Outputs formatted XML

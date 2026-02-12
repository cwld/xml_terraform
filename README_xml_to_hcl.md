# XML to HCL Converter

Converts XML (generated from Terraform HCL) back to Terraform HCL format.

## Installation

No additional dependencies required (uses Python standard library).

## Usage

```bash
python3 xml_to_hcl.py <terraform.xml>
```

## Example

Input (`example.xml`):
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

Output:
```hcl
resource "aws_instance" "example" {
  ami = "ami-123456"
  instance_type = "t2.micro"
}

output "instance_id" {
  value = "aws_instance.example.id"
}
```

## Features

- Converts XML back to valid Terraform HCL syntax
- Handles resources with type and name: `resource "type" "name"`
- Handles blocks with only name: `output "name"`, `variable "name"`
- Preserves nested block structures
- Properly formats attributes and values

## Supported Block Types

- **Two-label blocks**: `resource`, `data`, `module` → `type "resource_type" "name"`
- **Single-label blocks**: `output`, `variable`, `locals`, `terraform` → `type "name"`

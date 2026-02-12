# Terraform ⇄ XML Converter

## The Tool Nobody Asked For (But You're Here Anyway)

Welcome to the Terraform-XML converter suite! Because apparently HCL wasn't verbose enough for you.

## Why Would Anyone Do This?

Great question! Here are some totally legitimate reasons to convert your perfectly readable Terraform into XML:

### 1. **You Miss the 2000s**
Remember when everything was XML? SOAP APIs, config files, your grocery list? Those were the days. Now you can relive that glory by wrapping your infrastructure code in angle brackets.

### 2. **Job Security**
Nobody will dare touch your Terraform configs if they're in XML. Your coworkers will assume you're either a genius or completely unhinged. Either way, you're unfireable.

### 3. **You're Paid by the Character**
Why write `ami = "ami-123456"` when you could write `<ami>ami-123456</ami>`? That's 10 extra characters! At $0.01 per character, you just made an extra dime.

### 4. **Enterprise Compliance**
Your company's architecture review board only approves XML. They don't know what HCL is, and they're not about to learn now. Convert it, get the stamp, convert it back. Nobody needs to know.

### 5. **You Lost a Bet**
We've all been there.

### 6. **XML Parsers Are Your Love Language**
Some people collect stamps. Some people convert perfectly good DSLs into XML. We don't judge.

### 7. **You Want to Confuse Your CI/CD Pipeline**
"Why is Jenkins trying to parse XML as Terraform?" - Your DevOps team, probably

## Installation

```bash
pip install -r requirements.txt
```

## Usage

**To make things worse:**
```bash
python3 hcl_to_xml.py your_infrastructure.tf > your_infrastructure.xml
```

**To undo your mistakes:**
```bash
python3 xml_to_hcl.py your_infrastructure.xml > your_infrastructure.tf
```

## Features

✅ Converts HCL to XML  
✅ Converts XML back to HCL  
✅ Increases file size by approximately 40%  
✅ Makes code reviews take 3x longer  
✅ Confuses syntax highlighters  
✅ Gives your IDE an existential crisis  
✅ Makes grep results completely unreadable  
✅ Perfect for pranking coworkers  

## Real-World Use Cases

- **None identified yet**
- Please submit a PR if you find one
- Seriously, we're curious

## FAQ

**Q: Should I use this in production?**  
A: Define "should."

**Q: Will this make my infrastructure more reliable?**  
A: No, but it will make it more... angular.

**Q: Can I put this on my resume?**  
A: You can put anything on your resume. Whether you *should* is between you and your conscience.

**Q: Does this support Terraform 1.x?**  
A: It supports any Terraform version that can be parsed by python-hcl2. So... probably?

**Q: Why does the XML output look like a Christmas tree?**  
A: Because it's a gift. To someone. Maybe.

## Contributing

If you have ideas for making this even more unnecessarily complex, we're all ears. Bonus points if you can convert it to YAML first, then XML, then back to HCL.

## License

MIT - Because even we don't want to be held responsible for what you do with this.

## Disclaimer

This tool was created as a technical exercise and possibly as a joke. The authors are not responsible for:
- Angry DevOps teams
- Failed deployments
- Existential dread
- Questions from management about "why everything is in XML now"
- The heat death of the universe

## Acknowledgments

Thanks to:
- HashiCorp, for creating HCL so we could convert it to something worse
- The W3C, for XML
- You, for actually reading this far

---

*"Just because you can, doesn't mean you should."* - Everyone who sees this project

*"But what if we did anyway?"* - The authors

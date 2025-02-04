# Package Sorting Robot for Thoughtful Automation

A Python implementation of a package sorting system for robotic arms in an automation factory. The system categorizes packages based on their dimensions and mass into different handling stacks.

## Sorting Logic

Packages are sorted into three categories:

- **STANDARD**: Normal packages (not bulky or heavy)
- **SPECIAL**: Packages that are either heavy or bulky
- **REJECTED**: Packages that are both heavy and bulky

### Classification Criteria

- **Bulky Package**: 
  - Volume ≥ 1,000,000 cm³ OR
  - Any dimension ≥ 150 cm
- **Heavy Package**:
  - Mass ≥ 20 kg

## Usage

```python
from sort_packages import sort

# Example usage
result = sort(width=100, height=100, length=50, mass=10)
print(result)  # Output: "STANDARD"
```

## Running Tests

```bash
python test_sort_packages.py
```

## Project Structure

```
.
├── README.md
├── sort_packages.py
└── test_sort_packages.py
```

## Requirements
- Python 3.6+

## Contributing
1. Fork the repository
2. Create your feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details

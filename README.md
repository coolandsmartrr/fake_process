# fake_process

Print fictitious progress logs onto the terminal.

Example:
```
[2023-05-16 18:52:32 Process started.]
[2023-05-16 18:52:32 Initializing batch process...]
[2023-05-16 18:52:32 Loading data from source files...]
[2023-05-16 18:52:32 Data loaded successfully.]
[2023-05-16 18:52:32 Applying transformations to the data...]
[2023-05-16 18:52:32 Transformations applied successfully.]
[2023-05-16 18:52:32 Performing data validation...]
100%|██████████████████████████████████| 82/82 [00:00<00:00, 2339679.78epochs/s]
[2023-05-16 18:52:32 Data validation completed. No errors found.]
[2023-05-16 18:52:32 Starting batch processing...]
[2023-05-16 18:52:32 Process completed.]
[2023-05-16 18:52:32 Generating report...]
[2023-05-16 18:52:32 Report generated successfully.]
[2023-05-16 18:52:32 Finalizing batch process...]
[2023-05-16 18:52:32 Batch process finalized.]
[2023-05-16 18:52:32 Cleaning up temporary files...]
[2023-05-16 18:52:32 Temporary files cleaned up successfully.]
```

---

## How to run

```
cd [this directory]

python main.py

(or, for full window height:)
python main.py -c 
```

## Setup

Install dependencies
`pip install -r requirements.txt`
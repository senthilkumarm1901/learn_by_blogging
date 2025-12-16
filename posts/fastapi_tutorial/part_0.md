---
author: Senthil Kumar
badges: true
branch: master
categories:
- FastAPI
- FastAPI for AI

description: Sharing my learning notes on Python Type Hints, Python Concurrency and basics of FastAPI from official documentation
date: '2025-09-14'
draft: true
image: langgraph_logo.png
toc: true
title: "What I Learned about Python & FastAPI from the FastAPI Official Docs"
output-file: 2025-09-17-fastapi-genai-part-1.html
---


## 1. Important Python Precursors for FastAPI

### 1.1 Common Python Data Types 

> int, str, float, bool

#### Variables

##### Basic Annotations

- Declare types explicitly, even before assignment:
    
    ```python
    age: int = 1
    a: int  # okay without initialization
    ```
    
- Helpful in control flow:
    
    ```python
    child: bool
    if age < 18:
        child = True
    else:
        child = False
    ``` 
    
#### Useful Built-in Types

##### Basic Types

- You can annotate common types straightforwardly:  
    `int`, `float`, `bool`, `str`, `bytes` ([mypy.readthedocs.io](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html?utm_source=chatgpt.com "Type hints cheat sheet - mypy 1.17.1 documentation"))
    

##### Collections (Python 3.9+)

- Use bracketed types:
    
    ```python
    list[int], set[int], dict[str, float], tuple[int, str, float]
    tuple[int, ...]  # variable-length tuples
    ```
    

##### Older Python Versions (≤3.8)

- Use capitalized types from `typing`:  
    `List[int]`, `Dict[str, float]`, `Tuple[int, ...]` ([mypy.readthedocs.io](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html?utm_source=chatgpt.com "Type hints cheat sheet - mypy 1.17.1 documentation"))
    

##### Union & Optional Types

- Python 3.10+: use `|`:
    
    ```python
    list[int | str]
    x: str | None
    ```
    
- Pre-3.10:
    
    ```python
    Union[int, str]
    Optional[X]  # same as Union[X, None]
    ``` 

#### Functions

##### Basic Function Annotations

- Single argument:
    
    ```python
    def stringify(num: int) -> str: …
    ```
    
- Multiple args:
    
    ```python
    def plus(a: int, b: int) -> int: …
    ```
    
- No return value → use `-> None`; default values come after annotations ([mypy.readthedocs.io](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html?utm_source=chatgpt.com "Type hints cheat sheet - mypy 1.17.1 documentation"))
    

##### Callable Types & Generators

- Annotate function types:
    
    ```python
    x: Callable[[int, float], float] = f
    ```
    
- Generators yield `Iterator[...]`:
    
    ```python
    def gen(n: int) -> Iterator[int]: …
    ```
    

##### Advanced Function With Many Parameters

```python
def send_email(
    address: str | list[str],
    sender: str,
    cc: list[str] | None,
    bcc: list[str] | None,
    subject: str = '',
    body: list[str] | None = None,
) -> bool: …
```

##### Positional-only & Keyword-only Arguments  

```python
def quux(x: int, y: int, *args: str, **kwargs: float) -> None:
    ...
```

Here’s the breakdown:

### **1. Positional arguments**

- `x: int`
- `y: int`
    

These must always be passed **positionally** (unless you explicitly name them).  
Example:

```python
quux(1, 2)
```

👉 `x=1`, `y=2`

---

### **2. Variable positional arguments (`*args`)**

- `*args: str`
    

This collects **any extra positional arguments** after `x` and `y`.  
All those arguments must be `str`.  
Example:

```python
quux(1, 2, "a", "b", "c")
```

👉 `args = ("a", "b", "c")`

---

### **3. Variable keyword arguments (`**kwargs`)**

- `**kwargs: float`
    

This collects any **extra keyword arguments** into a dictionary.  
All their values must be `float`.  
Example:

```python
quux(1, 2, "a", "b", pi=3.14, e=2.71)
```

👉 `kwargs = {"pi": 3.14, "e": 2.71}`


### 1.2 Extra Python Data Types

- uuid, datetime.datetime, datetime.date,  datetime.time, datetime.timedelta, frozenset, bytes, Decimal


### 1.3 Classes as Data Types


---

### 1.3 Pydantic Models


---

### 1.4 Concurrency via `async/await`


#### 1.4.1 Simple Async Example

```python
from fastapi import FastAPI
import asyncio
app = FastAPI()

@app.get("/sleep3")
async def wait_3_sec():
    await asyncio.sleep(3)
    print("We waited for 3 seconds")
    return {"message": "Done waiting 3 seconds!"}

@app.get("/fast")
async def fast_response():
    print("Fast endpoint hit!")
    return {"message": "This was quick!"}
print("this statement is outside the python function")
```

#### 1.4.2 Async Example 2
```python
import asyncio
import time
from fastapi import FastAPI

app = FastAPI()


# ---------- "Kitchen" implementations ----------

def cook_burgers_sequential_way(duration: float = 3.0) -> str:
    """
    Blocking (synchronous) burger cooking.
    This uses time.sleep(), so while burgers cook,
    the server thread cannot process other requests.
    """
    print(f"👨‍🍳 [SYNC] Cook: Grilling burgers for {duration:.1f}s (blocking)...")
    time.sleep(duration)
    print("👨‍🍳 [SYNC] Cook: Burgers are ready!")
    return "🍔🍔"


async def cook_burgers_async_way(duration: float = 3.0) -> str:
    """
    Non-blocking (asynchronous) burger cooking.
    This uses asyncio.sleep(), so the event loop can
    switch to other tasks while waiting.
    """
    print(f"👨‍🍳 [ASYNC] Cook: Grilling burgers for {duration:.1f}s (non-blocking)...")
    await asyncio.sleep(duration)
    print("👨‍🍳 [ASYNC] Cook: Burgers are ready!")
    return "🍔🍔"


# ---------- "Customer" stories as endpoints ----------

@app.get("/sequential-burger")
def sequential_burger() -> str:
    """
    Sequential burger story (blocking).
    - Blocks the thread using time.sleep()
    - While this runs, no other request can be processed
      on this worker.
    """
    start = time.perf_counter()
    print("\n=== 🕙 SEQUENTIAL BURGER (blocking) ===")
    burgers = cook_burgers_sequential_way(3.0)
    elapsed = time.perf_counter() - start
    return f"🍔 Done in {elapsed:.2f}s (sequential, blocking)"


@app.get("/concurrent-burger")
async def concurrent_burger() -> str:
    """
    Concurrent burger story (async).
    - Uses asyncio.create_task()
    - Server can still process other requests while burgers cook.
    """
    start = time.perf_counter()
    print("\n=== ⚡ CONCURRENT BURGER (non-blocking) ===")
    burger_task = asyncio.create_task(cook_burgers_async_way(3.0))

    # "Flirting" while the burgers cook
    while not burger_task.done():
        await asyncio.sleep(0.9)
        t = time.perf_counter() - start
        print(f"💬 (t={t:.1f}s) Talking to your crush… burgers not ready yet.")

    burgers = await burger_task
    elapsed = time.perf_counter() - start
    return f"{burgers} Done in {elapsed:.2f}s (concurrent, async)"


@app.get("/flirt")
async def flirt() -> str:
    """
    A lightweight async endpoint to test concurrency.
    - Returns quickly if async concurrency is working.
    - Try calling this while /concurrent-burger is cooking.
    """
    await asyncio.sleep(0.2)
    return "😍 Still flirting while burgers are being cooked!"
```


---




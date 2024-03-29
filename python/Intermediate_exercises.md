1. Override Dunder methods such as new, init, str, repr, call, dict and del and create an object using new and init methods directly, print object name multiple times using call method. 
[Solution](creational-design-patterns/dunder_methods.py)
2. Create a "Thread safe Singleton" called 'Database' using allocators. [Solution](creational-design-patterns/singleton_allocator.py)
3. Implement a Singleton class called "Database" using decorator.  [Solution](creational-design-patterns/singleton_decorator.py)
4. Singleton using Metaclass.  [Solution](creational-design-patterns/singleton_metaclass.py)
5. Factory Design Pattern.  [Solution](creational-design-patterns/factory.py)
6. **Abstract Factory Design Pattern.   [Solution](creational-design-patterns/abstract_factory.py)** 
7. Builder Design Pattern.   [Solution](creational-design-patterns/builder.py)
8. **Prototype Design Pattern.   [Solution](creational-design-patterns/prototype.py)**
9. Adapter Design Pattern.   [Solution](structural-design-patterns/adaptor.py)
10. Bridge.   [Solution](structural-design-patterns/bridge.py)
11. Composite.   [Solution](structural-design-patterns/composite.py)
12. Decorator.   [Solution](structural-design-patterns/decorator.py)
13. Facade.   [Solution](structural-design-patterns/facade.py)
14. Flyweight.   [Solution](structural-design-patterns/flyweight.py)
15. Proxy.   [Solution](structural-design-patterns/proxy.py)
16. COR.   [Solution](behavioural-design-patterns/cor.py)
17. Command.   [Solution](behavioural-design-patterns/command.py)
18. Iterator.   [Solution](behavioural-design-patterns/iterator.py)
19. Mediator.   [Solution](behavioural-design-patterns/mediator.py)
20. Memento.   [Solution](behavioural-design-patterns/memento.py)
21. Observer.   [Solution](behavioural-design-patterns/observer.py) 

![Diagram](behavioural-design-patterns/observer.png)

22. State.   [Solution](behavioural-design-patterns/state.py)
23. Strategy.   [Solution](behavioural-design-patterns/strategy.py)
24. Template Method.   [Solution](behavioural-design-patterns/template-method.py)
25. Visitor.   [Solution](behavioural-design-patterns/visitor.py)
26. Singleton using monostate [solution](creational-design-patterns/singleton_monostate.py)
27. Python Mixins [Solution](misc/mixin.py)
28. Factorial using Recursion and Memoization [Solution](factorial/factorial_memoization.py)
29. Check if a given string is a palindrome using Reflections [Solution](palindrome/palindrome-reflections.py)
30. Implement a fibonacci series using Generators. [Solution](fibonacci/fibonacci_generators.py)
31. Factorial using Lambda function and functools.reduce [Solution](factorial/factorial_lambda_functools.py)
    1. Get the number 
    1. compute factorial using lambda
    1. compute factorial using lambda,reduce and range
    1. compute factorial using function,reduce and range
    1. a list named 'numbers' has the contents [3, 4, 6, 2, 1, 5], compute factorial using a factorial function and map without using for loop
    1. Check if any of the numbers in the above list is odd using 'any'
    1. Filter the above result list only for numbers divisible by 10
    1. Check if all of the numbers in the above list are even using 'all'
32. Functional Programming Exercises [Solution](misc/functional_programming.py)
    1. numbers = [9, 3, 49, 6, 28, 5, 20, 0, 3, 7,4, 2, 23, 34, 1, 8, 35]
    1. create a list with odd numbers > 7 using list comprehension
    1. Create a list of square of all numbers in the original list using map
    1. create a list with even numbers less than 7 from the original list with filter function
    1. strings = ["Learning"," Python"," Is"," Fun"]. Use .join to concatenate the strings
    1. Use functools.reduce to concatenate strings
    1. Use operator.add to concatenate strings
    1. Generate a list of random numbers
33. requests and urllib3 - CRUD Operations [Ref](https://dummyjson.com/products/add)
34. Descriptors [Solution](misc/descriptor.py)
35. Closures [Solution](misc/closures.py)
36. Palindrome using recursion [Solution](palindrome/palindrome-recursion.py) 
37. Context Managers [Solution](misc/context-manager.py)
38. Bitwise Operations [Solution](misc/bitwise.py) 
39. Currying Method [Solution](misc/currying_timeconversion.py)
40. Logging [Solution](misc/logger.py)
41. Python program to perform json operations [Solution](misc/json_operations.py)
    1. convert a dictionary to json string (json.dumps)
    1. json string to a new python dict (json.loads)
    1. write the same dictionary as a json file (json.dump)
    1. json file to a diff python dict(json.load)
42. Stack using List   [Solution](data-structures/stack_using_list.py)
43. Stack - balanced paranthesis [Solution](data-structures/stack_balanced_paranthesis.py)
44. Queue using List [Solution](data-structures/queue_using_list.py)
45. Linked List - Insert element at the head, end , middle, reverse [Solution](data-structures/linked_list.py)
46. Priority Queue [Solution](data-structures/priority_queue.py)
47. Tower of Hanoi [Solution](data-structures/tower_of_hanoi.py)
48. Modules (implement simplest MVC) [Solution](/mvc)
49. Unit Testing using unittest and pytest [Solution](/testing)
50. CLI using Argparse [Solution](misc/mcms.py)
51. Read an RSS Feed as XML and convert to csv [Solution](misc/rss_feed_xml.py)
52. Regex Operation [Solution](misc/regex.py)
53. Write a program to check the validity of password input by users [Solution](misc/pass_validation.py)
54. Binary Tree (pre-order,post-order and in-order traversal) [Solution](data-structures/binary_tree.py)
55. Binary Search [Solution](python/algorithms/binary-search.py) 
56. Linear Search Unsorted Input [Solution](algorithms/linear_search_unsorted.py)
57. Linear Search Sorted Input [Solution](algorithms/linear_search_sorted.py)
58. Stack using deque [Solution](python/data-structures/stack_using_deque.py)
59. Flask Rest API Calculator [Solution](rest-api/calculator.py)
60. Bubble Sort [Solution](algorithms/bubble_sort.py)
61. Insertion Sort [Solution](algorithms/insertion_sort.py)
62. Virtual Environments and Packaging
    1. Setup Virtual Environment using virtualenv and pyenv [Solution](setups/README.md)
    2. Creating Python packages and publishing to Pypi
63. A calculator web application using Flask [Solution](python/webapp/app.py)
64. Implement a system admin task using subprocess,os,sys modules [Solution](sysadmin/sysadmin.py)
65. create an ansible module to install packages using [Solution](ansible/package.yml)
66. create s3 bucket on localstack using boto3 [Solution](localstack/create_s3_buckets_boto3.py)
67. create Kafka topic, publish a message and consume the same using Python [Solution](devops/kafka_prod_cons.py)
68. Run a calculator API  using Serverless [Solution](serverless/serverless_framework)
69. Quick Sort [Solution](algorithms/quick_sort.py)
70. Use Python beautifulsoup to fetch the latest release of k8s from https://github.com/kubernetes/kubernetes [Solution](web_scraping/scraping.py)
71. Socket Programming [Solution](socket/socket_server.py)
72. kubernetes operator using kopf [Solution](devops/kopf-operator) 
73. A custom webhook using Python Flask API for Kubernetes Validating and Mutating Admission controllers [Solution](devops/admission_controllers)
74. Multi-Processing [Solution1](concurrency_parallelism/cpu_bound.py) and [Solution1](concurrency_parallelism/io_bound.py)
75. Multi-threading [Solution1](concurrency_parallelism/cpu_bound.py) and [Solution1](concurrency_parallelism/io_bound.py)
76. Asyncio & Coroutines [Solution1](concurrency_parallelism/cpu_bound.py) and [Solution1](concurrency_parallelism/io_bound.py)
77. cProfile, timeit and pstats and prometheus client library implementation [Solution1](webapp/app_with_profiling.py) and [Solution2](devops/prom_exporter.py)
78. Merge Sort [Solution](algorithms/merge-sort.py)
79. Selection Sort [Solution](algorithms/selection_sort.py)
80. LinkedList - Delete element at the head, end and middle, Traverse and Search [Solution](data-structures/linked_list_deletion.py)
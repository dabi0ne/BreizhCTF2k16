#!/usr/bin/python2.7
import readline

def filter_2(payload):
    """
    No double underscore
    """
    while "__" in payload:
        payload = payload.replace("__", "")
    return payload

def python_vm2():
    def exec_sandbox(payload):
        exec payload in scope

    scope = {"__builtins__" : {"dir" : dir, "_" : exec_sandbox}}

    while True:
        try:
            data = raw_input(">")
            if data is None:
                break
            data = filter_2(data)
            exec_sandbox(data)
        except EOFError:
            break
        except Exception as e:
            print("Something went wrong ", e)

if __name__ == '__main__':
    python_vm2()
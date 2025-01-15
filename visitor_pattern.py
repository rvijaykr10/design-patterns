"""
Usage: Allows adding new operations to existing class structures without modifying the structures.
"""

from fastapi import FastAPI


class Element:
    def accept(self, visitor):  # type: ignore
        pass


class ConcreteElementA(Element):
    def accept(self, visitor):  # type: ignore
        visitor.visit_concrete_element_a(self)  # type: ignore


class ConcreteElementB(Element):
    def accept(self, visitor):  # type: ignore
        visitor.visit_concrete_element_b(self)  # type: ignore


class Visitor:
    def visit_concrete_element_a(self, element):  # type: ignore
        pass

    def visit_concrete_element_b(self, element):  # type: ignore
        pass


class ConcreteVisitor(Visitor):
    def visit_concrete_element_a(self, element):  # type: ignore
        return "Visited ConcreteElementA"

    def visit_concrete_element_b(self, element):  # type: ignore
        return "Visited ConcreteElementB"


app = FastAPI()


@app.get("/visitor")
async def visitor():
    element_a = ConcreteElementA()
    element_b = ConcreteElementB()
    visitor = ConcreteVisitor()

    return {
        "element_a_visit": element_a.accept(visitor),  # type: ignore
        "element_b_visit": element_b.accept(visitor),  # type: ignore
    }

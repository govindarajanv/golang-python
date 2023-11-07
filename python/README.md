## Design Patterns 

| Design Pattern   | Type | Real Life Example   | Key Aspects | When to use
| -------- | ------- | -------- | ------- | ------- |
| Singleton  | Creational    | Database Object, Servlet  | static method and a counter    | Only one object needs to exist
| Factory | Creational     |Car Factory,Loggers  |     | Return object based on an input
| Abstract Factory   | Creational    |Beverage Maker, DeviceDrivers  | Abstraction over a family of factories    | family of factories
| Prototype   | Creational    |Car Factory   | Facory pattern with Deepcopy or clone    | Object creation is costlier
| Builder   | Creational    |Pizza Builder  | Multiple steps to complete the object building    | Object needs a lot of attributes

# Implementation Quick Reference


| Design Pattern   | Example Used | Implementation Hint
| -------- | ------- | ------- 
| Observer  | SNS Topic and Subscribers | Subscribers.notify & SNSTopic.notify_subscribers    
| State | Mobile Notifications Settings | Context as Alertsetting, Various Notifications mode (Alert, Silent and Vibration)     
| Strategy   | Deployment Strategies | Various Deployment Strategies and CDTool    
| Template Method   | Observability (Metric,Log and Trace) | Manage encapsulating capture, Publish and View    
| Visitor   | App Release Process | Each persona visiting to play their part in Release process

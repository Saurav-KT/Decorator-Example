### Python Property decorator, class decorator, static method decorator example.Use the following three decorators to define a property:
<hr>
<i> Property Decorator </i>
<ul>
  <li>@property : Declares the method as a property. </li>
  <li>@<property-name>.setter: Specifies the setter method for a property that sets the value to a property. </li>
  <li>@<property-name>.deleter: Specifies the delete method as a property that deletes a property. </li>
</ul>
<br>
<i> Class Decorator </i>
<section>
In Python, the @classmethod decorator is used to declare a method in the class as a class method that
can be called using ClassName.MethodName(). The class method can also be called using an object of the class.

The @ classmethod is an alternative of the classmethod() function.It is recommended to use the @ classmethod
decorator instead of the function because it is just a syntactic sugar.
</section>

<i>@classmethod Characteristics </i>
<ul>
<li>Declares a class method.</li>
<li>The first parameter must be cls, which can be used to access class attributes.</li>
<li>The class method can only access the class attributes but not the instance attributes.</li>
<li>The class method can be called using ClassName.MethodName() and also using object.</li>
<li>It can return an object of the class.</li>
</ul>


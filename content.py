COURSES = [ 
  {"title" : "Webpages, Documents, and Structure",
    "description" : ("This course dicusses basics of the web, structured documents and the use of stylesheets."),
    "lessons"  : [
    {"title"   : "The Basics of the Web and HTML",
    "description"   : "This lesson discusses the history of the web, HTML elements, and Inline vs. Block tags.",

    "concepts" : [
      {"title"      : "The Web - World Wide Web",
      "description" : "Invented in the 1990&#39;s and currently consists of approximately 30 Billion pages. <b>HTML</b> is the common language of the web. While many types of files such as Plain Text, HTML, Images, Videos, and Music, HTML is the main type of document found on the web. The web is comprised of documents linked together via <b>Hyper Links</b>. <br> <br>Components of the World Wide Web:<ul><li>HTTP &#45; The main protocol of the web.</li><li>Servers &#45; Computers that host files that make up the web.</li><li>Internet &#45; The Worlds largest computer network.</li><li>Browser &#45; A program that runs on your computer to display files found on the web</li></ul>"
      },
      {"title"      : "HTML - Hypertext Markup Language",
      "description" : """<b><em>HTML</em></b> is made up of:<ul><li>Text Content</li><li>Markup &#45; What it looks like</li>          <li>References to (e.g. images and videos)</li><li>Links to other pages</li></ul>Markup is achieved with the use of HTML "Tags."<br>Tags are often comprised of a set of Opening &lt;X> and Closing tags &lt;/X><br><br><span class="note">NOTE:</span><em><b>Void</b> Tags do not have a Closing Tag.</em>"""
      },
      {"title"      : "Elements and Attributes",
      "description" : "<b>Element</b> - Everything within a set of opening and closing tags.<br><b>Attribute</b> - Property of the HTML element."
      },
      {"title"      : "Inline / Block",
      "description" : """Examples of <span class="note">Inline</span> Tags<ul><li>&lt;b> - <b>Bold</b> - makes the text bold</li><li>&lt;em> - <b>Emphasis</b> - presents the text in an italicized form</li><li>&lt;span> - <b>Span</b> - ??? I will learn what this does later</li><li>&lt;a href> - <b>Anchor Tag</b> - Used for making links</li><li>&lt;img> - <b>Image Tag</b> - Used to include images. Consists of a source location (src=) and alternate text (alt=)</li>          <li>&lt;br> - <b>Line Break</b> - Used set contents on the next line</li></ul>Examples of <span class="note">Block</span> Tags<ul><li>&lt;p> - <b>Paragraph</b> - This tag is used to set the contents on a new line but also creates an invisible box around the text that can have additional parameters such as Vertical and Horizontal</li><li>&lt;div> - <b>Div</b> - ??? I will learn what this does later</li></uL>When learning to write code a great test browser has been provided by <a href="http://www.udacity.com/html_playground">Udacity.com</a>"""
      },
    ],
    },
    {"title"     : "Creating a Structured Document with HTML",
    "description"  : "Examining the structure of HTML, languages, and the concept of Boxifying.",
    
    "concepts" : [
      {"title"      : "Structure of an HTML Document",
      "description" : "&lt;!DOCTYPE HTML> - Doctype<br>&lt;html> - Opening html tag<br>&lt;head> - Includes metadata i.e CSS        <br>&lt;title> - Title of the page that appears at the top of the browser window<br>&lt;/head><br>&lt;body> - Content of the web page<br>&lt;b> content &lt;/b><br>&lt;/body><br>&lt;/html> - Closing html tag<div>          HTML documents are comprised of a Tree-Like Structure</div>"
      },
      {"title"      : """HTML and CSS are both <em>"Languages"</em>""",
      "description" : "<ul><li>HTML controls the <em><b>structure</b></em> of a web page</li><li>CSS controls the <em><b>style</b></em> of a web page (how it looks).</li></ul>When programmers talk about the &quot; DOM &quot; (Document Object Model), they are talking about the tree-like structure of a page.<div>All elements are rectangular</div>"
      },
      {"title"      : "Boxify",
      "description" : "<b>Boxifying a Design</b> &#45; The process of visualizing all the elements of a web page as independent rectangles or <em><b>boxes</b></em>.<p>When <em><b>Boxifying</b></em> a web page Boxes can also have boxes within boxes, within boxes, etc. This can also be referred to as <em>Nested</em> boxes</p>"
      }
    ]
    },

    {"title"     : "Adding Style to Structure with CSS",
      "description"  : "Exploring tools to validate HTML and CSS code and discuss Divs, Spans, Classes, and Ids more indepth.",
      "concepts" : [
      {"title"      : "CSS",
      "description" : """CSS is code written to control the "style" of HTML elements.<p>Cascading Style Sheets (CSS) is a set of rules to describe the formating of elements. When CSS is used, it allows a programmer to reduce code to describe how each element is displayed by referencing a specific style sheet to obtain the attribute for the     element.<p>The term <em>cascading</em> is important as CSS utilizes <em>Most Specific Rule Applies.</em> This method is also referred to as <em>inheritance.</em><p>One of the <span class="note">GREATEST</span> assets derrived from using CSS is the ability for the programmer to avoid repetition within the code!"""
      },
      {"title"      : "Inheritance",
      "description" : """Wikipedia describes <a href="http://en.wikipedia.org/wiki/Cascading_Style_Sheets#Inheritance">Inheritance</a> as <em>the mechanism by which properties are applied not only to a specified element, but also to its descendants.</em> This functionality is made possible by the &quot;Tree-Like&quot; structure mentioned earlier. Each element will inherit specific rules from it&#39;s &quot;ancestor&quot; or element it has been &quot;nested&quot; within. Wikipedia goes on to say, &quot;descendant elements inherit text-related properties, but box-related properties are not inherited.&quot;<p>According to wikipedia, examples of inherited properties are:<ul><li>Color</li><li>Font</li><li>Letter-spacing</li><li>Line-height</li><li>List-style</li><li>Text-align</li>   <li>Text-indent</li><li>Text-transform</li><li>Visibility</li> <li>White-space</li><li>Word-spacing</li></ul><p>Examples of properties NOT inherited are:<ul><li>Background</li><li>Border</li><li>Display</li><li>Float and Clear </li><li>Height and Width</li> <li>Margin</li><li>Min- and Max-height and Width</li><li>Outline</li> <li>Overflow  </li><li>Padding</li><li>Position</li><li>Text-decoration</li><li>Vertical-align</li><li>Z-index</li></ul><p>When using CSS a programmer will utilize selectors and define attributes. Selector - Defines the elements to apply the style<p>A programmer can assign a style by selecting the elements by tag or even by class.<p>Style format is &quot;Attribute&quot; : &quot;Value&quot;<p>P {<br> Color:Red<br>}<p>IMPORTANT: A great link to CSS References is found at https://developer.mozilla.org/en-US/docs/Web/CSS/Reference <p>How do I include CSS Styling in my web page? here are three ways you can do this.<ul><li><b>Method 1:</b> write CSS in the "&lt;head>" of your HTML Inside the &lt;head> element, add a &lt;style> element. Write your CSS in the &lt;style> element and then put the HTML for the rest of your page below.</li><li><b>Method 2:</b> Link your HTML to a separate CSS file This adds another step, but it lets you stay more organized when working on larger projects. To do this: 1. Write all of your structural HTML in one file (let's call it main.html). 2. In a separate file (let's call it main.css), put all of your CSS code. 3. Add a &lt;head> element to the top of your HTML. 4. Add a &lt;link> tag inside the &lt;head> element. Since &lt;link> is a "void tag" you don't need to add a closing &lt;/link>. 5. Add the following attributes to your &lt;link>: * rel="stylesheet" * type="text/css" * href="main.css"</li><li><b>Method 3:</b> Write your style inline with your HTML This is generally a very bad idea because it leads to lots of repeated code. But you may see code that uses this method so it's good to be familiar with it.</li></ul>"""
            },
      {"title"      : "Divs, Spans, Classes, Ids",
      "description" : "<ul><li>Use Divs to control layout. Div tags bump things to the next line.</li><li>Use Spans to control style without affecting the layout.</li> <li>ID provides a method to uniquely identify an element. Two elements within the page cannot the same ID.</li><li>Classes are used for many items on a page that wl be styled similarly.</li></ul>"
      },
      {"title"      : "Diagram of the Box",
      "description" : "HTML elements are boxes and each box has 4 components.<br>- ->Margin &#45; Clears the area around the border and is transparent. &quot;Space between boxes&quot;<br>--- ->Border &#45; Inherited from the Color property of the box<br>----- ->Padding &#45; Clears the area arounf the content and is affected by the background color of the box<br>-------- ->Content &#45; Image or text that appears on the website<p>There are two techniques you can use to help deal with sizing issues.<br>1. Set sizes in terms of percentages rather than pixels.<br>2. Set the box-sizing attribute to border-box for every element.<p>1. Divs are block elements (as opposed to inline), so by default they take up the entire width of a page.<br>2. Adding the rule display: flex; to the appropriate CSS will override this behavior and let divs appear next to each other."
      },
      {"title"      : "Verifying HTML and CSS",
      "description" : """<br>To verify HTML: <a href="http://validator.w3.org/#validate_by_input">http://validator.w3.org/#validate_by_input</a><br>To verify CSS: <a href="http://jigsaw.w3.org/css-validator/#validate_by_input">http://jigsaw.w3.org/css-validator/#validate_by_input</a>"""
      }
    ]
    }
    ]

  },
  
  {"title"    : "Telling Computers What To Do",
    "description"   : ("Programming, Variiables, Strings, Functions, Loops, Debugging, Lists, and Problem Solving"),
    "lessons"    : [
    {"title"     : "Basics of Programming",
      "description"  : "Computer programming, languages, python, Backus-Naur, Expressins, and Debugging",
      "concepts" : [
          
      {"title"      : "Computer",
      "description" : "A Computer can do anything we want it to do as long as we tell it what to do. We tell computers what to do by writing programs that give the computer a specific sequence of instructions.<p>"
      },    
      {"title"      : "Computer Program",
      "description" : "A Computer Program is th method we use to provide the computer with a specific set of instructions to perform some useful task. Common business applications, web browsers, games, etc. are all examples of computer progrrams.<p>"
      },    
      {"title"      : "Programming Language",
      "description" : "A programming language is utilized to write computer programs. Python, Visual Basic, Perl, Java, are all examples of programming languages.<p>"
      },    
      {"title"      : "Python",
      "description" : "Python is a computer programming language, that when Run will utilize a Python Interpreter to to convert the code into instruction the computer understands.<p>"
      },    
      {"title"      : "Grammar",
      "description" : "Grammar is utilized to specify what is Correct and Incorrect in a language. Grammar hold true and is present regqarding computer programming languages as well. When writing a program for a computer, the instructions must be written precisely and follow all the grammatical rules of the specified language. If written poorly, the computer cannot interpret what the programmer meant for the computer to perform. An example of programming grammar for many programming languages is Backus-Nour Form.<p>"
      },    
      {"title"      : "Backus-Naur",
      "description" : "Backus-Naur Form - Is used to precisely describe exactly the language in a way that is very simple and very precise. &lt;Non-Terminal> &rarr; replacement Derivation - Starting with Non terminal and replace until only terminals are left. Python Grammar for Arithmetic Expressions<ul><li>Expression &rarr; Expression Operator Expression</li> <li>Expression &rarr; Number</li> <li>Operator &rarr; +</li> <li>Operator &rarr; *</li><li>Number &rarr; 1,2,3...</li><li>Expression &rarr; (Expression)</li> </ul><p>"
      },    
      {"title"      : "Python Expressions",
      "description" : """A Python expression is any statement that follows all of the python program language rules.<a href="https://www.udacity.com/course/viewer#!/c-ud552-nd/l-3527838955/e-48704311/m-48736065" target="_blank">Python Grammar Video</a>"""
      },    
      {"title"      : "Debugging",
      "description" : """Debugging is the process of evaluating computer programming code to determine if it will work successfully or not. Whe the code fails to perform the intended task, this is considered a "bug". A programmer will evaluate the code assessing for correct syntax to determine and fix erros."""
      }
    ],
    },


    {"title"     : "Variables and Strings",
      "description"  : "Variables, Strings, Indexing, Subsequences, and Elements",
      
      "concepts" : [

      {"title"      : "Variables",
      "description" : """Variable must be assigned a value<p>Assignment Statement: Name = Expression<p>A convention that most programmers follow is that variables should not begin with a capital letter.<p>Defined variables can be changed, thus the nature of the "Vari"able.<p> Variables are useful because:<ul> <li>They improve code readability by using names that make sense to humans.</li><li>They give us a way to store the value of important data.</li><li>They give us a way to change the value of something (like in the line days = days-1)</li> </ul><p>"""
      },
      {"title"      : "Strings",
      "description" : "Strings are a sequence of characters within a single or double quote. A single quote can also be contained within a string as long as the string begins and ends with a double quote. <p><ul> <li>Operator '&#43;' </li><li>'&#43;' results in concatenation</li><li>&lt;string> + &lt;string> &rarr; concatenation of the two strings </li><li>String + Integer produces an error (i.e. test+1)</li><li>However, String * Interger produces the string 'x' number of times as defined by the integer.</li></ul><p>"
      },          
      {"title"      : "Indexing Strings",
      "description" : "<ul><li>&lt;string> [expression>]</li><li>'udacity'[0] &rarr; 'u'</li><li>0,1,2,3,4,5,6</li><li>'udacity'[1+1] &rarr; 'a'</li><li>name = 'Dave'</li><li>name[0] &rarr; 'D'</li></ul><p> print name[4]<br>This command produces an error because the current value of 'name' is 'dave' that contains only an index of 0-3.<br>IndexError: string index out of range<p> Print name[-1]<br>The negative operator starts at the end of the string. [-1] is the last character of the string.<p>"
      },    
      {"title"      : "Selecting Subsequences",
      "description" : """&lt;string> [expression>] &rarr; one-character string<br> Number<p> Start stop<br>&lt;string> [expression>:expression>] &rarr; (see below)<br>Number Number<p>&rarr; Sting that is a sub-sequence of the charaters in 's' starting from position start, and ending with position stop -1.<p> "text".find("t", 1) and in this case, there are two parameters<p><ul><li>print "Example 2: using a variable to store first location"</li><li>first_location = "test".find("t") # here we store the first location of "t"</li><li>print "test".find("t", first_location+1) # then we use that location to find the second occurrence.</li></ul> <p> <ul><li>print "Example 3: using find to get rid of exclamation marks!!"</li><li>example = "Wow! Python is great! Don't you think?"</li><li>first = example.find('!')</li><li>second = example.find('!', first + 1)</li><li>new_string = example[:first] + example[first+1:second] + example[second+1:]</li><li>print new_string # oops, I should probably replace the !s periods</li><li>new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]</li><li>print new_string</li></ul>"""
      },    
      {"title"      : "Elements",
      "description" : "HTML documents are made up of HTML 'elements'."
      }
    ],
    },


    {"title"     : "Input, Function, Output",
      "description"  : "Functions - How to write them and why they are useful",
      
      "concepts" : [
      {"title"      : "Functions",
      "description" : "According to webopedia, a <b>function</b> is a type of <b>procedure</b> or <b>routine</b>. Some programming languages make a distinction between a <b>function</b>, which returns a value, and a <b>procedure</b>, which performs some operation but does not return a value. Most programming languages come with a prewritten set of functions that are kept in a library."
      },
      {"title"      : "How to Make a Function",
      "description" : """A function (aka procedure) is comprised of a procedure and operands (or arguments)<br> procedure> (input>, input>, ...)<br> Operands or Arguments<p>When making a function (or procedure), the function must first be defined. To do this, we use the keyword "def". The def statement is then followed by the name of the function. Finally, th function parameters are listed in parentheses. The parametersare empty values until the function is called at a later time in the code.<p><ul> <li>You must begin the line with def (lowercase)</li><li>After def you must give a function name.</li><li>Next, you must have a set of parentheses with the required parameters inside.</li><li>The line must end with a : colon</li></ul><p>Example:<br>def rest_of_string (s) :<br> return s[1:]<p><div class="note">Note: The RETURN statement is extremely IMPORTANT! If a return is not included in the building of the function, no value will be output.</div><p>"""
      },
      {"title"      : "How to Use a Function",
      "description" : "When using a function, the function can be called directly by listing the name f the function and include the desired values to provide for the expected parameters.<p> print rest_of_string ('audacity')<p>"
      },
      {"title"      : "When You Should Write a Function",
      "description" : """According to <a href="www.openbookproject.net"> OpenBookproject.net</a>, creating a new function gives you an opportunity to name a group of statements. Functions can simplify a program by hiding a complex computation behind a single command andby using English words in place of arcane code."""
      },
      {"title"      : "Why Functions are So Valuable",
      "description" : """FUNCTIONS ALLOWPROGRAMMERS TO AVOID REPETITION<p>According to Adam at Udacity.com, Functions are tools that programmers can create and reuse forever! Once you've defined a function once, you never have to define it again.<p>According to OpenBookProject.net, creating a new function can make a program smaller by eliminating repetitive code. For example, a short way to print nine consecutive new lines is to call three_lines three times.<p><div class="example_code">def say_hello(name):<br>greeting = "Hello " + name + '!'<br>return greeting<p>print say_hello("Tony")<p>Output:<br>"Hello Tony!"</div><p> In the first line, 'name' is a "parameter" of the function say_hello<p><div class="example_code">def add_two_numbers(number_1, number_2):<br>return number_1 + number_2<p>print add_two_numbers(4, 3)<br>print add_two_numbers(2,print<br>add_two_numbers(0, 9) <p>Output:<br>7<br>8<br>9</div>"""
      },
      {"title"      : "Procedure Composition",
      "description" : "Procedure composition often calls a procedure multiple times within itself.<p>Most procedure code is written in this manner:<p>def square (n):<br>Return n*n<p>X=37<br>Print square(square(x))<p><br>_____________<br>def sum3(a,b,c)<br> return a+b+c<br><br>print sum3(3,8,32)"
      }       
    ],
    },


    {"title"     : "Control Flow & Loops: If and While",
      "description"  : "Example using Loops",
      
      "concepts" : [
      {"title"      : "Loops",
      "description" : """while &lt;test expression>: # can be executed 0,1,2,... times as long as the test expression is true &lt;block><p>if &lt;test expression>: #can be executed 0 or 1 times<br>&lt;block></P>Example of While Loop<p># This code demonstrates a while loop with a "counting variable"<br>i = 0<br>while i &lt; 10:<br>print i<br>i = i+1"""
      }
    ],
    },


    {"title"     : "Debugging",
      "description"  : "A discussion of Debugging Strategy",
      
      "concepts" : [
      {"title"      : "Debugging",
      "description" : """<p><h3>Udacity's 5 Debugging Strategies</h3><p> <span class="note">Examine error messages when programs crash</span><br> The last line of Python Tracebacks will tell you what went wrong. Reading backwards from there will tell you more about where the problem occurred.</P><p><span class="note">Work from example code</span><br> If your modified code doesn't work, comment it out and do step-by-step modifications to the example code until it does what you want.</P><p><span class="note">Make sure examples work</span><br> Just because you find example code doesn't mean it will work in your system. Check the example code you're using to make sure it behaves the way you expect.</p><p><span class="note">Check (print) intermediate results</span><br> When your code doesn't crash, but doesn't behave as expected, add print statements to your program to see where in the code things stop behaving correctly.</p><p><span class="note">Keep and compare old versions</span><br> When you have a working version of your code, save it before you add to the code. This will give you something to go back to if you introduce too many new bugs.</p>"""
      }
    ],
    },


    {"title"     : "Structured Data: Lists and For Loops",
      "description"  : "An overview of strings vs. lists, Mutation, Append Method, For Loops, IN and NOT IN", 
      "concepts" : [
      {"title"      : "Differences between Strings and Lists",
      "description" : "A <b><em>String</em></b> is a sequence of characters.<br> <br>s='yabba!'<br>s[0] &rarr; 'y'<br>s[2:4] &rarr; 'bb'<p>A <b><em>List</em></b> is a sequence of anything.<br><br>p=['y','a','b','b','a']<br>p[0] &rarr; 'y'<br>s[2:4] &rarr; ['b','b']<p>"
      },    
      {"title"      : "Mutation",
      "description" : "Another difference between Strings and Lists is that Lists allow for Mutation<br><br><br>Mutation means that we can alter asingle element within a list without haing to create an entirely new list. <br>Example: <br>p=['H','e','l','l','o']<br>p[0]='Y'<br> &rarr; 'Y','e','l','l','o'<br>q=p #This means that now both p and q both refer to the same list. <p>Another example of Mutation of a List:<br><br>stooges = ['Moe','Larry','Curly']<br>stooges[2] = 'Shemp' <br>print stooges<p>"
      },
      {"title"      : "Append Method",
      "description" : """<p>Another tool built within Python that allows the programmer to add an item to the end of a list is called the Append Method.<br>stooges=['Moe','Larry','Curly']<br>stooges.append()'Shemp')<br> The list 'stooges' now contains 'Moe','Larry','Curly', Shemp'<p>"""
      },
      {"title"      : "List Addition and Length",
      "description" : """List Addition allows the programer to add the contents of two lists together to form one longer new list.<br><br> Example: <br>[0,1] + [2,3] &rarr; [0,1,2,3]<p>Length<br><br>Length is a tool within Python that tells the computer to return a value equal to the count of individual items within a list.<br><br>Examples of Length:<br><br>len([0,1]) &rarr; 2<br>len(['a',['b',['c']]]) &rarr; 2<br>len("Udacity") &rarr; 7<p>"""
      },
      {"title"      : "For Loops",
      "description" : """<br><b><em>FOR</em></b> Loops are used to loop through every element within a list without having to use a WHILE loop which uses more code.<p>Examples: print "EXAMPLE 1: We can use for loops to go through a list of strings"<br>example_list_1 = ['a', 'b', 'c', 'd']<br>for thing in example_list_1:<br>&nbsp;&nbsp;&nbsp;&nbsp;print thing<br> <br> print "EXAMPLE 2: We can use for loops on nested lists too!"<br>example_list_2 = [['China', 'Beijing'],<br>&nbsp;&nbsp;&nbsp;&nbsp; ['USA' , 'Washington D.C.'],<br>&nbsp;&nbsp;&nbsp;&nbsp; ['India', 'Delhi']] <br>for country_with_capital in example_list_2:<br>&nbsp;&nbsp;&nbsp;country = country_with_capital[0]<br>&nbsp;&nbsp;&nbsp;capital = country_with_capital[1]<br>&nbsp;&nbsp;&nbsp;print capital + ' is the capital of ' + country<p>"""
      },
      {"title"      : "Index",
      "description" : "<br>Index is a tool within Python that can be used to find the positional location of a specific value within a list if it exists within that list.<br><br>if &lt;value> is in the &lt;list>, returns the first position where &lt;value> is found in &lt;list> ... otherwise, produces an error.<br><p>"
      },
      {"title"      : "IN",
      "description" : "<br><b>IN</b> is a tool within Python that can be used to determine if a specific value is found within a list.<br><br> &lt;value> in &lt;list><br> if &lt;value> is in the &lt;list>, output is <b><em>True</em></b>. Otherwise, output is <b><em>False</em></b>.<p>"
      },
      {"title"      : "NOT IN or NOT",
      "description" : "<br> NOT IN or NOT are also tools within Python that can be used to determine if a specific value is found within a list.<br><br> &lt;value> not in &lt;list><br><br> This can also be written as:<br><br>not &lt;value> in &lt;list>"
      }
    ],
    },


    {"title"     : "Problem Solving",
      "description"  : "How to undrstand a problem and identifying a method to  solve it.",
      "concepts" : [
      {"title"      : "Understanding A Problem",
      "description" : "A problem is defined by the relationship between possible inputs and the desired output. <p><b>Rules for Problem Solving</b><p><ol type=1><li>Don't Panic</li><li>What are the Inputs?</li><ol type=i><li>Use defensive programming to check the validity of the inputs.</li></ol><li>What are the Outputs</li> <li>Solve the Problem</li><ol type=i><li>Understand the Inputs</li><li>Understand the Outputs</li><li>Understand the Relationship - some examples</li><li>Consider systematically how a human solves the problem</li><li>Work through some examples by hand</li></ol><li>Simple Mechanical Solution</li> <ol type=i><li>*Don't Optimize Prematurely!</li><li>Simple and Correct</li> <li>Develop Incrementally as you go.</li></ol></ol>"
            },
    ]
    }
    ] 
  },

  {"title"    : "The Power of Abstraction",
    "description"   : ("Object Oriented Programming, its benefits and how it relates to HTML and CSS. Calsses, Variables, Inheritance, Method Overriding, Libraries, FROM vs. Import, External Python Packages, Built-In Functions, and Google Style Guide."),
    "lessons"    : [
    {"title"   : "Object Oriented Programming",
    "description"   : "Object Oriented Programming, its benefits and how it relates to HTML and CSS. Calsses, Variables, Inheritance, Method Overriding, Libraries, FROM vs. Import, External Python Packages, Built-In Functions, and Google Style Guide.",
    
    "concepts" : [
      {"title"      : "Object Oriented Programming",
      "description" : """<br>Object Oriented Programming (OOP) is basically programming by using objects. The objects communicate with each other by sending messages. The programmer defines objects to manipulate by use of a Class. Objects are actually instances of the classor subclasses, each with attributes and methods. The programmer will expect an input, then have the objects interract with each other and change variables to produce a desired output. Common languages that utilize Object Oriented Programming arePython, Java, Perl, C++, and PHP.<p>A great description of OOP, <a href="https://www.youtube.com/watch?v=SZqLEDH0x7A">Object Oriented Programming for Dummies</a>, by Anthony Bucyk and Joseph Lersch<p>Defining a function and calling a single function multiple times throughout the program will reduce or eliminate uneccessary duplicate code. Additionally, by using the concept of inheritance, the programmer can further reduce duplicate code by sharingattributes within classes and subclasses. <p><span class="note">NOTE:</span>A function within a class is also called a "Method".<p>See Al Sweigart's blog For a great <a href="http://inventwithpython.com/blog/2014/12/02/why-is-object-oriented-programming-useful-with-an-role-playing-game-example/">example using a Role Playing Game</a> that describes the use of Classes,Constructor, Methods, and Inheritance."""
      },
      {"title"      : "Abstraction",
      "description" : """<br>The whole concept of Object Oriented Programming is to "abstract" the more intricate code required to "make things work" and allow the programmer to simply think in terms of objects and manipulation of those objects.<p>According to Whatis.com - In object-oriented programming, abstraction is one of three central principles (along with encapsulation and inheritance). Through the process of abstraction, a programmer hides all but the relevant data about an object in order to reduce complexity and increase efficiency. (whatis.techtarget.com/definition/abstraction)"""
      },
      {"title"      : "Benefits of Object Oriented Programming",
      "description" : """<br>Maintenance<br>Reusability<br>Modifiability<p> The benefits of using OOP for large programming projects is that is allows code to be reused thoughout the program, the code is easily modified, and maintenance by various programmers can be easily achived due to the inherent nature of the way the code is written. For instance, any programmer familiar with OOP can look at another programmer's code to determine what attributes and behaviors are found within a class. The programmer can further analyze and identify the various classes and subclass relationships."""
      },
      {"title"      : "OOP as it relates to HTML and CSS",
      "description" : """<br>The easiest connection to make between OOP and HTML and CSS is by viewing how a programmer can use ABSTRACTION &#40;Abstract Thinking&#41; to  reduce the amount of HTML code simply by using a CSS file to contain formatting and behavioral attributes about a class of text. For example, a CSS file could designate Classes such as "Header", "Title", and "Description" each with its own unique font color, size, behavior, etc. To create all of the code in one single file would be quite lengthy to provide code for each attribute each time it is needed in HTML. By using CSS, the programmer only has to identify the specified class by its name from within the associated CSS file, then all the attributes are applied by HTML.<br><br>Cascading Style Sheets by very nature exhibit similarity to Object Oriented Programming by means of inheritance.  Just as Objects and derived classes inherit attributes from parent or superclasses, CSS employs this same concept of passing attributes &#40;Most Specific Rule Applies&#41;. Strategic placement of attributes allows the programmer to reduce the amount of code as attributes are inherited."""
      },
      {"title"      : "Vocabulary of Common Terms used with OOP",
      "description" : """<b>Encapsulation</b> - is term used for combining data and behaviors of an object into the "black box" often referred to in OOP.<br><br><b>Method</b> - is simply a defined function belonging to an Object defined within a Class that can be called. <br><br><b>Module</b> - A module is nothing more than a set of functions and varibles within a file. The aspects of a module can be imported by another file for use within that file.<br><br><b>Library</b> - A library in OOP often contains standard modules built for various commonly used functions that can simply be imported for use by the programmer.  A programmer can also create their own library and even utilize newly created modules.<br><br><b>Class</b> - A "class" is a set of specific instructions that include various attribute parameters that can be used and is designed to create an "instance" of an object. A class can have data and methods.<br><br><b>Object</b> - Data Structures that are comprised of attributes and methods (procedures). An object procedure can be used to modify an attribute of the same object.<br><br><b>Instance</b> - An "instance" is an actual object that has been initialized and created based on the specifications outlined in the associated "class". An "instance" can be customized uniquely from other instances created from the same "class".<br><br><b>Constructor</b> - When an instance is created, the "Constructor" of the Class is called and is also the "__INIT__" method. The constructor uses the keyword "SELF" which represents itself or the instance being created. <br><br><b>Self</b> - When a constructor is called from the class, "self" refers to the instance of the class being created.<br><br><b>Instance Variable</b> - All of the variables associated with an instance are called "instance variables". These are unique to the variable and can be accesed from within the class can be accessed with the keyword "self". Outside the class,the instance variables can be accessed by using the actual instance name when outside the class.<br><br><b>Instance Method</b> - All functions that are defined inside a class are associated with an instance, and include the first argument as "self".<br><br> It is good practice to keep Class definition in a separate file and only call or use the class from another file."""
      },
      {"title"      : "Classes",
      "description" : """<p>When classes are called the "init" or initialize function is actually called that creates space within memory for a new instance of the Class.<p>What is a class? A "class" is a set of specific instructions that include various attribute parameters that can be used and is designed to create an "instance" of an object.<p>What is an instance of a class? An "instance" is an actual object that has been initialized and created based on the specifications outlined in the associated "class". An "instance" can be customized uniquely from other instances created from the same "class".<p>Classes are like blueprints that contain information about an object Multiple instances of a Class can be created from from this "blueprint".<p>Another analogy to explain classes and their instances would be how an automobile manufacturer details all of the requirements and specifications to manufacture a specific vehicle model. These specifications would be analogous to the "class".<p>An "instance" in this automobile analogy would be how a buyer could customize the color, interior upgrades, stereo, engine size, and various other options and actually have the vehicle made. The customized actual vehicle would be considered the "instance".<p> A wise friend from Udacity, Stacy, provided another analogy for me as follows &#40;WARNING - May Make You Hungry&#41;:<p>"Another good example is that class, object, and instance align with cookie cutter, shaped cookie, and a particular cookie. A cookie cutter is meant to create cookies of a certain shape &#40;maybe a star shape&#41;. So you end up with star-shaped cookies &#40;objects&#41; from it. But maybe this cookie I pick up &#40;an instance&#41; is made with chocolate-chip cookie dough, while maybe this other one &#40;another instance&#41; is made with peanut butter cookie dough."""
      },
      {"title"      : "Variables",
      "description" : """""<p>Variables can be defined at multiple levels when using classes. Varibles specific to an instance of a class should be defined within the instance. Varibles that will be shared among many instances should be defined at the Class level.<p>In Python, some Classes come with pre-defined class variables. One such variable is "__doc__". When "__doc__" is called, the program will search for any text found within the triple qoutes (i.e. ""xxxxx"").<p>Additional pre-defined class variables are __name__ and __module__."""""
      },
      {"title"      : "Inheritance",
      "description" : """<p>Inheritance is the concept that attributes are passed from the parent instance to the child instance. The child instance can also have unique attributes and in some programming languages,inherit attributes from more than one parent class to which the child instance belongs.<p><span class="note">NOTE:</span> The parent class is sometimes called the Superclass or Base Class, while the child class is sometimes called the subclass or derived class.<p>The principles of inheritance can allow certain variables placed at appropriate levels reduce the need to have all the variables held at the instance levels. Additionally, child classes can be placed within an existing parent class and inherit varibles thus reducing the need to repeat variables at the child level.<p><a href="http://learnpythonthehardway.org/book/ex42.html">Learn Python The Hard Way</a> is a great explanation for distinguishing Classes vs. Objects.<p><b>Example:</b><br>classParent<br>--last_name<br>--eye_color<p>classChild<br> --number_of_toys"""         
      },
      {"title"      : "Method Overriding",
      "description" : "<p>Methods can also appear within parent and child classes. When a method in the child (or sub class) is called by the same name as it is within the parent class, this is called Method Overriding. The programmer can specify to ignore the inherited method and use only the method as it is called within the subclass."
      },
      {"title"      : "Recap of Class Objects",
      "description" : "<p><b>Create...</b><br>brad = turtle.Turtle #An object of Turtle<br>quotes = open(file) #An object of file<br>connection = urllib.urlopen() #A File like object<p><b>Do...</b><br>Brad.forward(100)<br>Quotes.read()<br>Connection.read()"
      },
      {"title"      : "Programming Concepts - Libraries",
      "description" : "<p>As mentioned previously, a library in OOP often contains standard modules built for various commonly used functions that can simply be imported for use by the programmer.<p>Each common programming language will contain it own library for a programmer's use.<p>A programmer can also create their own library to utilize or even import someone else's library."
      },
      {"title"      : "FROM VS. IMPORT (PYTHON)",
      "description" : """<p>The From statement allows a programmer to import specific attributes from a module into the current namespace rather than the entire module.<p><b>Example Format:</b><br><span class="example_code">from module import attribute</span><p> If the programmer wants to import <b>ALL</b> names / attributed from the module, the following format can be utilized:<br><span class="example_code">from module import *</span>"""
      },
      {"title"      : "External Python Packages",
      "description" : """<p>Twilio is an external python package that can be downloaded and used to send text messages. <p>There are thousands of external Python packages that can be used. A complete list of all external python packages can be viewed <a href="https://pypi.python.org/pypi?%3Aaction=browse">here</a>.<p>The entire twilio python code can be viewed <a href="https://github.com/twilio/twilio">here</a>."""
      },
      {"title"      : "Python Built In Functions",
      "description" : """<p>Python built-in functions can be found <a href="https://docs.python.org/2/library/functions.html">here</a>. <p>These Python modules are not located in the module OS, but rather in a separate Module<p><img src="python_built_in.jpg" alt="Python Built in Functions" height="334" width="740"><p>Example use of Python Built-In function<p><span class="example_code">pow(x, y[, z])</span><p>Return x to the power y; if z is present, return x to the power y, modulo z (computed more efficiently than <span class="example_code">pow(x, y) % z)</span>. The two-argument form pow(x, y) is equivalent to using the power operator:<span class="example_code">x**y</span>.<p>Created example file with the following code: <br><span class="example_code">print pow (2,4)</span> <br>Result &rarr; 16<p> Additional Python functions (Used in the Profanity Checker Project from Udacity):<p><b>Open</b> &#45; Opens a file from a location on the computer<br> Example: <span class="example_code">quotes = open("C:\dtect_profanity\movie_quotes.txt")</span><br> Open is actually a Python Built-In function. When called it actually executes "init" to create an "object" of "file" (This is similar to creating objects of "Class".)<p><b>Read</b> &#45; Reads the contents of a text file that has been opened by the program.<br> Example: <span class="example_code">contents_of_file = quotes.read()<br> Print (contents_of_file)</span><p><b>Close</b> &#45; Closes a file that has been opened by the program<br>Example: <span class="example_code">quotes..close()</span><p><span class="note">Note:</span> It is good convention to close programs that your program has opened. <p>Profanity checker webite query URL: <br><a href="http://www.wdyl.com/profanity?q=shot">http://www.wdyl.com/profanity?q=shot</a><p>After "&#61;" enter the word in question and await the response.<p>urllib is its own module found in python. Urlopen is a function found inside urllib."""
      },
      {"title"      : "Other Examples of Functions",
      "description" : """<p><span class="example_code">Webbrowser.open (python)</span> This is a function that takes any web link you enter and open the browser within python. <br><b>Example:</b><br><span class="example_code">webbrowser.open("http:www.youttube.com")</span><p><span class="example_code">time.sleep(10)</span> This function causes the program to wait a specified number of seconds.<p>You have to Import the webbrowser function before it can be used. To do so, add the statement:<br><span class="example_code">import webbrowser</span><br><span class="example_code">import time</span><p>Use <span class="example_code">ctrl + c</span> within the IDLE Python window if you want to stop the current program from running.<p><span class="example_code">os.rename(src, dst)</span><br>Rename the file or directory src to dst.<p><span class="example_code">os.getcwd</span><br>This function gets the name of the current working directory.<p><span class="example_code">os.chdir</span><br>This function allows the programmer to change the directory to be utilized within a program."""
      },
      {"title"      : "Google Style Guide",
      "description" : """<p>The Google Style Guide provides conventions to programmers around the world regarding how to maintain desired conventions for various programming languages.<p>For example, the Google Style Guide for Python recommends that when defining a class, the first letter should be capitalized. This is not a requirement in python, but rather a preference published by Google.<p> Here is the link to the <a href="https://google-styleguide.googlecode.com/svn/trunk/pyguide.html">Google Style Guide for Python</a><p> Additionally, the Google Style Guide for Python also recommends that when a variable is going to remain constant, (i.e. the Movie Ratings in the Udacity Movie trailer project, the variable should be defined using ALL CAPS.<p>Example:<span class="example_code">VALID_RATINGS = ["G", "PG", "PG-13", "R"]</span>"""
      },

    ]
    }
    ] 
  },



  {"title"    : "The Full Stack",
    "description"   : ("How the web works, forms, security, Data Structures, String Substitution, Escaping, Redirection and Templates."),
    "lessons"    : [
    {"title"   : "Networks",
    "description"   : "What are Networks",
    
    "concepts" : [
      {"title" : "Networks",
      "description" : "Network - A group of entities that can communicate, even though they are not ALL directly connected.<br>Humans have been using networks for over 3,000 years.<br>When making a network one would need to consider the following:<ul><li> Way to encode and interpret messages</li><li>Way to route messages</li><li>Rules for deciding who gets to use resources</li></ul>"},
      {"title" : "Measuring Networks",
      "description" : "Latency - Time that it takes for a message to get from the source to the destination. Measured in time (i.e. seconds / milliseconds.<br>Bandwidth - Amount of information that can be transmitted oer unit of time. Measured in Bits per second. (Mbps)<br><br>Bit - Smallest unit of information.<br>Protocol - A set of rules that people agree to that tell how two entities can talk to each other."},
    ],
    },


    {"title"   : "Document Structure",
    "description"   : "Basic HTML Document Structure",
    "concepts" : [
      {"title" : "Concept title aa",
      "description" : "<DOTYPE..... get notes from previous section in overall project<br>&#60;head><br>[Title, CSS, JS]<br>&#60;/head><br><br>&#60;body><br>[Content]<br>&#60;/body>"},
    ],
    },


    {"title"   : "URLs",
    "description"   : "What are URLs?",
    "concepts" : [
      {"title" : "URLs",
      "description" : "URL - Uniform Resource Locator<br>http:    //   www.udacity.com /<br>Protocol      Host        Path<br><br>Given the protocol- ftp, the host - www.udacity.com, and the path /about, what is the correct url?<br>ftp://www.udacity.com/about"},
    ],
    },


    {"title"   : "Query Parameter",
    "description"   : "Query - The GET Parameter",
    "concepts" : [
      {"title" : "Query Parameter (GET Parameter)",
      "description" : """Example:<br>http://example.com/foo?p=1   - The "&#63;p=1" is the query<br>Name = value (or p=1)<br><br>While the first query is always separated from the URL by the question mark "?" ; all of the following queries are then<br><br>separated by the ampersand "&".<br><br>Example of secondary query<br>http://example.com/foo?p=1&q=neat"""},  
    ],
    },


    {"title"   : "Fragments",
    "description"   : "Web Fragments",
    "concepts" : [
      {"title" : "Fragments",
      "description" : "Is used to reference a particular part of the page being viewed. <br><br>The fragment  IS NOT SENT TO THE SERVER when you make a request.  It only exists in the browser.<br>Example: <br>http://www.example.com/foo#fragment<br><br>If a FRAGMENT is present in conjuction with a Query Parameter, the FRAGMENT always appears last.<br>Example:<br>http://www.example.com/foo?p=1#fragment"},  
    ],
    },


    {"title"   : "Port",
    "description"   : "The networking port being utilized",
    "concepts" : [
      {"title" : "Port",
      "description" : "When making a web request to a server, you will need the address and the port.  By default, the port is implied to be port 80, but you can change the port during the request by specifying it in the URL.<br><br>Example:<br>http://localhost:8000/<br><br>URL Quiz Result:<br>Identify the components for <br>http://example.com:80/toys?p=foo#blah<br><br>host:   example.com<br>protocol: http<br>fragment: #blah<br>query:    ?p=foo<br>port:     80"},
    ],
    },


    {"title"   : "HTTP",
    "description"   : "HTTP - Hyper Text Transfer Protocol",
    "concepts" : [
      {"title" : "HTTP",
      "description" : "HTTP - Hypertext Transfer Protocol<br><br>When http://www.example.com/foo is sent over the web, the following request are actually being sent:<br><br>GET  /foo  HTTP/1.1 (request line)<br>(Method) (Path) (Version)<br><br>Method - They tyoe of request being made to the server. The most common method is 'GET'. Another method is 'POST'<br><br>Path - Path refers to the actual document being requested rom the server.<br>Version - Version identifies the - always HTTP followed by the version number.  In most casses it is 1.1 but ometimes 1.0"},
    ],
    },


    {"title"   : "HTTP Request",
    "description"   : "HTTP Request",
    "concepts" : [
      {"title" : "HTTP Request",
      "description" : "When sending a request, all items are sent at once including all headers.<br>GET /foo?p=1  HTTP/1.1  Headers:"},
    ],
    },


    {"title"   : "Headers",
    "description"   : "What are Headers and what do they do?",
    "concepts" : [
      {"title" : "Headers",
      "description" : "Host: www.example.com  (Comes from the URL and is required in HTTP/1.1) Since the web server machine can host multiple websites, we must specify which website we are requesting the document from.<br><br>User - Agent: chrome<br>Describes who is making the request and is usually the name of the browser.<br><br>Taking the Oath<br>I promise to use User-Agents appropriately when writing software.  <br>The reason for this is that some individuals pretend to be browsers and are actually performing potentially inappropriate <br>or resource consuming tasks that can hurt the website being utilized.<br><ul>Examples of Valid Headers:<li>Host: www.hipmunk.com</li><li>User-Agent: ignore me I'm a spammer</li><li>i-made-this-up: whatever</li></ul>"},
    ],
    },


    {"title"   : "HTTP Responses",
    "description"   : "What are HTTP Responses?",
    "concepts" : [
      {"title" : "HTTP Responses",
      "description" : "Request<br>GET /foo HTTP/1.1<br><br>Response<br>HTTP/1.1      200            OK   (status line)<br>       (Status Code)  (Reason Phrase // Just an english language description of the Status Code)  <br>Example Status Codes:<li>200  OK</li><li>302  Found (Document found, but located somewhere else)</li><li>404  Not Found</li><li>500 Server Error (Server broke while trying to handle the request)</li><br>Status codes begin with 2,3,4 or 5<li>2 - Success</li><li>3 - You may need to do something different technically to find this document</li><li>4 - Means there was an error on the Browser side (i.e. requesting a document that does not exist)</li><li>5 - Means there was an error on the server side</li><br>Headers commonly included with HTTP Responses<br>Date:    Tue Mar 2012 04:33:33 GMT (date and time the request happened)<br>Server:   Apache /2.2.3   (Name of the server that is handling the response // Instructor at Udacity advised he typically does not include this header as it i or falsifies the info as basically giving away free information to potential hackers)<br>Content-Type:   text/html;<br>Content-Length: 1539  (Not strictly required but tells the browser how long the doc is)"},
    ],
    },


    {"title"   : "Servers",
    "description"   : "What do servers do?",
    "concepts" : [
      {"title" : "Servers",
      "description" : "Purpose: respond to HTTP requests<br><br>Two main types of services:<br>Static - Pre-written file(i.e. image) <br>Dynamic - responses built on-the-fly built by a programs that are running (Also known as Web Applications)"}
    ],
    },


    {"title"   : "HTML Forms",
    "description"   : "What are HTML Forms?",
    "concepts" : [
      {"title" : "HTML Forms",
      "description" : "&lt;form><br>&lt;input> (Adds a Textbox) [Input tag can take an attribute called'name' ] (i.e. &lt;input name='name'>) <br>&lt;/form><br><br>Another input attribute is 'type'<br>&lt;input type='submit'> creates a Submit Button<br>&lt;input type='text'>"},
    ],
    },


    {"title"   : "Password",
    "description"   : "How to add passwords in forms.",
    "concepts" : [
      {"title" : "Password",
      "description" : "&lt;input type = 'password'> Useful for entering passwords into text boxes.<br>*Be aware that passwords submitted in this method are not sent securely on their own as they are sent just like any other parameter and may be visible in the URL."},
    ],
    },


    {"title"   : "Checkbox",
    "description"   : "How to add a checkbox to a form.",
    "concepts" : [
      {"title" : "Checkbox",
      "description" : "&lt;input type='checkbox'> Provides a checkbox for the user to select.  <br>If selected cb = ON, <br>if not selected, the cb is not passed to the URL"},
    ],
    },

    {"title"   : "Radio",
    "description"   : "What is a Radio in reference to web forms",
    "concepts" : [
      {"title" : "Radio",
      "description" : "&lt;input type='radio'> Provides a checkbox for the user to select.  If selected cb = ON, if not selected, the cb is not passed to the URL"},
      {"title" : "Radio as a Group",
      "description" : "To make a set of Radio elements behave as a group, give them all the same name.<br><br>Example: <br>&lt;input type='radio' name='y'><br>&lt;input type='radio' name='y'>"},
      {"title" : "Radio Element Values",
      "description" : "In order to identify which radio element is selected when passing the information to the URL is to use the 'value' parameter.<br><br>Example: <br>&lt;input type='radio' name='y' value='one'><br>&lt;input type='radio' name='y' value='two'>"},
      {"title" : "Radio Element Labels",
      "description" : "The 'Label' element is used to give the user an idea of what the radio button or other element is referring to."}
    ],
    },

    {"title"   : "Dropdown",
    "description"   : "LUsing Dropdown elements in forms",
    "concepts" : [
      {"title" : "Dropdown",
      "description" : "&lt;select name='a'><br>&lt;option>One&lt;/option><br>&lt;option>Two&lt;/option><br>&lt;option>Three&lt;/option><br>&lt;/select>"},
      {"title" : "Dropdowns with Different Values Passed Other than what is Displayed",
      "description" : "&lt;select name='b'><br>&lt;option value='1'>One&lt;/option><br>&lt;option value='2'>Two&lt;/option><br>&lt;option value='3'>Three&lt;/option><br>&lt;/select>"},
    ],
    },

    {"title"   : "ACTION",
    "description"   : "What does ACTION have to do with forms?",
    "concepts" : [
      {"title" : "ACTION",
      "description" : "Another attribute is 'ACTION' that controls where a form is submitted to.<br>&lt;form action='/foo'><br><br>URL encoding takes place by adding pluses instead of spaces when inputting more than one value in an input attribute."},
    ],
    },

    {"title"   : "Modulus Operator",
    "description"   : "What is a Modulus Operator",
    "concepts" : [
      {"title" : "Modulus Operator",
      "description" : "The Modulus Operator: This is an operator that is represented with the &#37; sign.<br>It is similar to other operators like +, -, *, or / that every programming language has.<br><br>The purpose of Modulus is to get outputs within the correct range.<br>To do this, modulus takes a number and maps it to the range based on the remainder when you divide that number.<br>&lt;number> % &lt;modulus> --> &lt;remainder><br>14 % 12 = 2 because when you divide 14 by 12 have a remainder of 2<br><br>Examples:<br>15 % 12 = 3<br>15 % 11 = 4<br>4 % 3 = 1<br>3 % 4 = 3 (Since 3 is not divisible by 4, the entire quantity of the original 3 is left a the remainder)"},
    ],
    },

    {"title"   : "Dictionary",
    "description"   : "Dictionary as a Data Structure",
    "concepts" : [
      {"title" : "Dictionary",
      "description" : "Dictionaries: This is another data structure, similar to a Python List. <br><br>Strings and Lists in comparison with Dictionaries<br>String <br>Sequence of characters<br>'hello'<br>Strings are Immutable<br>s[i] gives the ith character in the string<br><br>List <br>List of elements<br>[alpha',23]<br>Lists are Mutable<br>p[i] gives the ith element of p<br>p[i] = u replaces the ith element of p with the value u<br><br>Dictionary<br>A set of <key, value> pairs<br>{'hydrogen':1,'helium':23}<br>Dictionaries are Mutable<br>d[k]  ('k' is the key so this operation will give the value associated with 'k' in d)<br><br>Dictonary Example<br><br>elements = { 'hydrogen': 1,  'helium': 2, 'carbon': 6}<br>print elements<br><br>Since dictionaries are NOT ORDERED, the result will not be in the order in which we entered them as the result displays <br><br>alphabetically based on the key.<br><br>print elements['helium']<br> --> 2<br><br>print elements['lithium']<br><br>--> KeyError: 'lithium' (This is because 'lithium' is not found in the dictionary.)"},
      {"title" : "Searching for an Item in a Dictionary",
      "description" : "You can perform a search to see if an element is in the dictionary with the following code:<br>print 'lithium' in elements<br>--> False"},
      {"title" : "Adding an Item to a Dictionary",
      "description" : "You can ADD an item to the Dictionary with the following code:<br>elements['lithium'] = 3<br>elements['nitrogen'] = 8"},
      {"title" : "Changing the Value of a Key in the Dictionary",
      "description" : "You can change the Value of a Key in the Dictionary with the following code:<br>elements['nitrogen'] = 7<br>This is similar to adding, but in this case the Key is already in the dictionary so it just updates the value."},
      {"title" : "Dictionary Quiz",
      "description" : "EXAMPLE DICTIONARY QUIZ:<br>Define a Dictionary, population,<br>that provides information<br>on the world's largest cities.<br>The key is the name of a city<br>(a string), and the associated<br>value is its population in<br>millions.<br><br>   Key     |   Value<br> Shanghai  |   17.8 <br> Istanbul  |   13.3<br> Karachi   |   13.0<br> Mumbai    |   12.5<br><br>population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}<br>print population ['Karachi']<br><br>--> 13.0 <br><br>This Dictionary could have also been created with code as in this example (See Image <br>Dictionary_Example)**************************<br><br>The Values can be Anything.  Values can even be other Disctionaries as in the example code below.<br>(See Image Dictionary_Within_Dictionary)************************<br><br>NOTE: In other programming languages, python dictionaries are similar to Hash Tables.  Be sure to check StackOverflow for equivalents."}
    ],
    },

    {"title"   : "Google App Engine",
    "description"   : "Components of Google App Engine",
    "concepts" : [
      {"title" : "Handler",
      "description" : "One term that is often encountered when writing python code for use with Google App Engine and Templates, is 'Handler'.  <br>On way of describing what 'handler' does is to think of it as a gateway or router in networking.  Handlers are created for <br>each specific /path in your website.  The handler talls something like Google App Engine how to find the desired content.  <br>If a /path is entered that is not listed with a Handler, the web browser will generate 404 Error, unless the programmer <br>has establisged a generic /path in the YAML file such as 'url:.*'."},
      {"title" : "GET VS. POST",
      "description" : "GET<br>- Parameters in URL<br>- Used for fetching documents<br>- Subject to the maximum URL length<br>- Ok to cache<br>- Shouldn't change the server (you should be able to make the same get request over and over and not have to change the server.)<br><br>POST<br>- Parameters in Body<br>- Used for updating Data<br>- Have no maximum length, but may be limited by the server<br>- Not ok to cache<br>- Ok to change the server"},
    ],
    },

    {"title"   : "Web Application Hacked?",
    "description"   : "Try using Input Validation",
    "concepts" : [
      {"title" : "Input Validation",
      "description" : "Validation<br>Verifying what we received is what we expected to receive<br><br>Just because you have a form with a checkbox, does not mean that someone cannot send parameters with arbitrary junk directly.<br><br>Ensure your server knows how to handle input that is not expected."},
    ],
    },

    {"title"   : "String Substitution",
    "description"   : "How does String Substitution work?",
    "concepts" : [
      {"title" : "String Substitution",
      "description" : "String substitution can be used to make generating HTML convenient.<br><br>Example:<br>'&lt;b>c&lt;/b>'<br><br>'&lt;b>%s&lt;/b>'  % VARIABLE  ---> replaced the contents with '%s'. This will substitute the contents of the variable in to %s within the &lt;b> tags.<br><br>Example using the string substitution variable:<br>a = 'some bold text'<br>'&lt;b>%s&lt;/b>''  % a<br><br>Output:<br>---> &lt;b>some bold text&lt;/b><br><br>String Substitution Code Example:<br> Write a function 'sub1' that, given a <br> string, embeds that string in <br> the string: <br> 'I think X is a perfectly normal thing to do in public.'<br> where X is replaced by the given <br> string.<br> The function should return the new string.<br><br>given_string = 'I think %s is a perfectly normal thing to do in public.'<br>def sub1(s):<br>    return given_string % s<br>    <br>print sub1('running') <br> => 'I think running is a perfectly normal thing to do in public.'    <br>print sub1('sleeping') <br> => 'I think sleeping is a perfectly normal thing to do in public.'"},
      {"title" : "String ubstitution with Multiple Variables",
      "description" : "'text %s text %s' % (VAR1, VAR2)<br><br>Write a function 'sub2' that, given two strings, embeds those strings in the string: 'I think X and Y are perfectly normal things to do in public.'<br>where X and Y are replaced by the given strings. The function should return the new string.<br><br>given_string2 = 'I think %s and %s are perfectly normal things to do in public.'<br>def sub2(s1, s2):<br>    return given_string2 % (s1,s2)<br>print sub2('running', 'sleeping') <br>=> 'I think running and sleeping are perfectly normal things to do in public.'<br>print sub2('sleeping', 'running') <br>=> 'I think sleeping and running are perfectly normal things to do in public.'"},     
      {"title" : "String Substitution Using Multiple Values Multiple Times",
      "description" : "This function employs the use o a dictionary.'text %(NAME)s text' % {'NAME':value}<br><br>Write a function 'sub_m' that takes a name and a nickname, and returns a string of the following format: <br>'I'm NICKNAME. My real name is NAME, but my friends call me NICKNAME.'<br><br>given_string2 = 'I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s.'<br>def sub_m(name, nickname):<br>    return given_string2 % {'name':(name),'nickname':(nickname)}    <br><br>print sub_m('Mike', 'Goose') <br> => 'I'm Goose. My real name is Mike, but my friends call me Goose.'"},
    ],
    },

    {"title"   : "Input Values",
    "description"   : "How to use Input Values",
    "concepts" : [
      {"title" : "Input Values",
      "description" : "&lt;input type = 'text' value = 'cool'>   ---> The Default Value is value = 'cool'<br><br>This can be useful to enter as values in the form to eliminate the need for the user to re-enter values from a previous attempt.  Default values can also be used to pre-fill a form with commonly used entries.<br><br>Example from Udacity &lt;input name ='month' value='%(month)s'>"},
    ],
    },

    {"title"   : "Escaping",
    "description"   : "Not just getting away for awhile!",
    "concepts" : [
      {"title" : "Escaping",
      "description" : "Hackers who understand how a page is rendered with unprotected Input Value fields can manipulate the fields with unintended HTML tags to completely change how the document is displayed in the browser (i.e adding New Text, images, etc.).<br><br>Escaping can be utlized to help protect input fields by 'escaping' or 'changing' commonly used HTML code into general text values that will not be interpreted as HTML code.<br><br>Examples of escaping HTML:<br><br> --> &quot;<br>> --> &gt;<br>< --> &lt;<br>& --> &amp;<br><br>Following the rules of Escaping, if you want to render text that displays &=&amp; in an HTML page, you would need to write the following:<br>&amp; = &amp;amp;  <br><br>Translated  &amp; (&) '=' &amp; (&) 'amp;'<br><br>Example of a defined function that escapes html by using a list:<br><br>Implement the function escape_html(s), which replaces<br>all instances of:<br> > with &gt;<br> < with &lt;<br> ' with &quot;<br> & with &amp;<br> and returns the escaped string<br> Note that your browser will probably automatically render your escaped text as the corresponding symbols, but the grading script will still correctly evaluate it.<br><br>def escape_html(s):<br>for (i,o) in (('&','&amp;'), <br>              ('>','&gt;'),<br>              ('<','&lt;'),<br>              ('"',"&quot;")):<br>    s=s.replace(i,o)<br>return s<br><br>print escape_html(">")<br>print escape_html("<")<br>print escape_html('"')<br>print escape_html('&')<br>print escape_html('<b>Insert Malicious Code Here</b>')<br><br>--> &gt;<br>--> &lt;<br>--> &quot;<br>--><br> &amp;<br>--> &lt;b&gt;Insert Malicious Code Here&lt;/b&gt;<br><br>Alternate Method using CGI within the Python Library that yields the same result:<br><br>import cgi<br>def escape_html(s):<br>    return cgi.escape(s, quote = True)"},
    ],
    },

    {"title"   : "Redirection",
    "description"   : "What is Redirection and why is it useful?",
    "concepts" : [
      {"title" : "Redirection",
      "description" : "Reasons you will want to use redirection are to avoid the limitations experienced when rendering the server response HTML as a POST<br><br> - Can't share a success link (in the example)<br> - Can't reload the page without an annoying message from the browser asking if you want to resubmit the form (This is experienced when the page is drawn with a POST)<br><br>In Udacity's Date form example, redirect will be employed to point the user to another HTML file rather than sending a response via POST back to the user's browser. <br><br>*****(Insert Redirection Image*****  <br><br>It is nice to redirect after a form submission for the following reasons:<br>- So that reloading the page doesn't resubmit the form<br>- So that we can have distinct pages for forms and success pages"},
    ],
    },

    {"title"   : "Templates",
    "description"   : "What are Templates?",
    "concepts" : [
      {"title" : "Templates",
      "description" : "Benefits of Templates:<br>Separate different types of code<br>Make more readable code<br>More secure websites (using escaping)<br>HTML that is easier to modify<br><br>A template library is a library to build complicated strings (html).<br><br>jinja2 - A template library built into Google App Engine<br><br>Additional information about Jinja2 can be found at jinja.pocoo.org ************"},
      {"title" : "Variable Substitution",
      "description" : "Syntax for substituting variables in jinja2 is to utilize double curly braces.<br>{{variable}}<br><br>'{{' is similar to requesting to Print<br>Example:<br>&lt;h2>Hello, {{name}}&lt;/h2>"},
      {"title" : "Statement Syntax",
      "description" : "Statement Syntax in Jinja2<br>{% statement %}<br>output<br>{% end statement %}<br><br>Example:<br>{% if name =='steve'%}  <--- Notice there is no colon<br>Hello, Steve!<br>{% else %}<br>Who are you?<br>{% endif %}  <---- Note there is no space"},
      {"title" : "For Loop Syntax",
      "description" : "{% for statement %}<br>body<br>{% endfor %}<br>Example Code: (FizzBuzz) Print Fizz if n is divisible by 3, Buzz if divisible by 5, and FizzBuzz if divisible by 3 and 5  <br><span class='example_code'><br>&lt;form>  <br>&lt;ol><br>{% for x in range(1,n+1) %}<br>&lt;li><br>{% if x % 15 == 0 %}<br>FizzBuzz<br>{% elif x % 3 == 0 %}<br>Fizz<br>{% elif x % 5 == 0 %}<br>Buzz<br>{% else %}<br>{{ x }}<br>{% endif %}<br>&lt;/li><br>{% endfor %}<br>&lt;/ol><br><br>&lt;!--{% if n == 1 %}<br>n equals 1<br>{% else %}<br>n does not equal 1<br>{% endif %}--><br>&lt;/form></span>"},
      {"title" : "Escaping HTML in Jinja2",
      "description" : "Escaping HTML in Jinja2 will help prevent against unwanted HTML code when rendering. There are two methods to do this.<br><br>Method 1:<br>Add ' | escape' to your substitution. 'Escape' is actually calling on a built in filter, of which there are many filters built into jinja2.  The escape filter will then replace html tags with equivalent displays by using items such as <br>'&rarr;'. See previous section titled 'Escaping' for more information.<br>Example:<br>&lt;li>{{ item | escape}}&lt;/li><br><br>Method 2:<br>When initializing jinja2 , add the instruction 'autoescape = True)' to the statement.  This will ensure all substitutions are automatically escaped.<br>Example Initialization statement:<br>jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)"},
      {"title" : "Escaping Override",
      "description" : "Another Option is available if you need to actually display the substitution with the HTML. To do this, just add '| safe' to the substitution.<br>Example:<br>&lt;li>{{ item | safe}}&lt;/li><br><br>***Note: You can add this even if Autoescape is enabled<br><br>Helpful Tips:<br>- Always automatically escape variable when possible<br>- Minimize code in templates<br>- Minimize HTML in code (if you need to have HTML, put it in a template) This helps keep your code and HTML separate."},
      {"title" : "Template Inheritance",
      "description" : "To illustrate this concept, think of how most web pages have a header and footer that seems to remain constant as you navigate through the webpages of that site.  To do this, the header and footer are likely just a Template, that is called for each new page, and then there are sub-templates that are generating the content that is changing from page to page.<br>Example: (Notice the jinja2 'block content' code) <br>&lt;!DOCTYPE html><br><br>&lt;html><br> &lt;head><br>   &lt;title>Udacity Templates<br> &lt;/head><br><br>  &lt;body style='margin: 0'><br>   &lt;h1 style='background-color: #ddd; color: #888; margin: 0 height: 50px'><br>     Udacity Templates<br>   &lt;/h1><br><br>    {% block content %}<br>   {% endblock %}<br>  &lt;/body><br>&lt;/html><br>Example of how to add content from another template into previous template (Shopping_list.html) - Notice the required <br><br>'Extends, block, and endblock' jinja2 code. Use View Source to see how the HTML is actually generated.<span class='example_code'><br>{% extends 'base.html' %}<br><br>{% block content %}<br>&lt;form><br>  &lt;h2>Add a Food&lt;/h2><br> &lt;input type='text' name='food'><br>  {% if items %}<br>    {% for item in items %}<br>     &lt;input type='hidden' name='food' value='{{item}}'><br>   {% endfor %}<br>  {% endif %}<br> &lt;button>Add&lt;/button><br><br>  {% if items %}<br>    &lt;br><br>   &lt;br><br><br>   &lt;h2>Shopping List&lt;/h2><br>    &lt;ul><br>     {% for item in items %}<br>       <li>{{ item }}&lt;/li><br>      {% endfor %}<br>    &lt;/ul><br>  {% endif %}<br>&lt;/form><br><br>{% endblock %}</span><br><br>NOTE: The same template inheritance was added to /fizzbuzz.  Remember that to execute fizzbuzz, modify the URL as follows:<br>'http://localhost:10080/fizzbuzz?n=15'"},
      {"title" : "*args and *kwargs for Google App Engine Project",
      "description" : "If you are using CSS (which we are) you must secify a folder such as in the example:<br> Insert this above the libraries in the yaml file<br>- url: /static<br>static_dir: static<br>this must also go above the url: .*<br>scripts: main.app<br><br>*args will unpack lists or tuples // an ordered data structure that you can index by number and goes in order.<br>Example List: [1,2,3,4,5]<br>Example Tuple: (1,2,3,4,5)<br>Often used with for loops.<br><br>**kwargs is used for things that have a key value set, where the Key is what the parameter is going to be, and the Value <br><br>is the value the parameter will take. "},
    ]
    }
    ] 
  }
]

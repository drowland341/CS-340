How do you write programs that are maintainable, readable, and adaptable?


Writing maintainable, readable, and adaptable programs requires a combination of good coding practices and thoughtful design. One of the most effective strategies I use is to break down functionality into modular components. In the case of my CRUD Python module from Project One, I encapsulated all database operations—such as creating, reading, updating, and deleting data—into separate functions within a class. This separation of concerns made the code more organized and allowed me to reuse the module in Project Two without any significant changes.

I followed best practices for naming conventions and commenting. Each function and variable had descriptive names, making the code easy to understand at a glance. Additionally, I included docstrings and inline comments to explain the purpose of more complex sections of code. This ensures that other developers, or even I, after some time...can revisit the code and quickly understand how it works. Adding error handling was another important aspect, as it helped make the system more resilient by catching exceptions and providing useful error messages when operations failed.

The advantage of working in this way is that the CRUD module can be adapted to any project requiring database connectivity. Since the database operations are generic, the module can be reused in applications beyond the animal shelter database, like managing user accounts, handling product inventories, or processing customer orders. This modular, reusable approach saves development time in future projects.



How do you approach a problem as a computer scientist?


When approaching a problem as a computer scientist, my first step is always to break the problem into smaller, more manageable tasks. For example, when working on the Grazioso Salvare dashboard, I first focused on the core database operations. I developed the CRUD Python module that would serve as the backbone for data retrieval and manipulation. Afterward, I tackled the user interface, integrating the module with the dashboard’s interactive widgets. This methodical approach ensured that each component worked correctly before moving on to the next.

In this project, my approach differed from previous assignments because it required me to think more about real-world application and user interaction. While many of my previous assignments focused on algorithms or backend development, this project required a user-centric view and considering how the user would filter data, interact with the dashboard, and visualize results. I applied principles of user interface design by making the dashboard intuitive and responsive to the user’s selections. In the future, I would apply the same technique of breaking down client requirements into smaller components. I would also make use of design patterns like MVC (Model-View-Controller) to separate data, logic, and presentation for better scalability and maintainability.



What do computer scientists do, and why does it matter?


Computer scientists solve complex problems by leveraging technology and programming to create innovative, efficient solutions. They take vast amounts of data or complex requirements and design systems that simplify decision-making and enhance productivity. In the case of the Grazioso Salvare project, the dashboard I developed allowed the company to quickly filter and analyze data about dogs in shelters, helping them to make informed decisions about which animals to train for search-and-rescue operations.

The work I did in this project can be applied across many industries. Whether it’s programming computer chips in embedded systems, managing customer data for a business, optimizing logistics for a shipping company, or filtering rescue dogs for a nonprofit, computer scientists design solutions that empower organizations to operate more efficiently. In a world increasingly driven by data, being able to analyze and manipulate large datasets quickly and accurately is essential. My work on this project provided Grazioso Salvare with the tools to make data-driven decisions, which directly impacts their ability to save lives and meet their mission goals.

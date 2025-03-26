<h1 class="code-line" data-line-start="0" data-line-end="1"><a id="Task_Tracker_CLI_0"></a>Task Tracker CLI</h1>
<p class="has-line-data" data-line-start="2" data-line-end="3">Instructions</p>
<ol>
<li class="has-line-data" data-line-start="3" data-line-end="6">
<p class="has-line-data" data-line-start="3" data-line-end="5">Clone the repository<br>
<code>git clone https://github.com/ElaniZanlucas/Task-Tracker.git</code></p>
</li>
<li class="has-line-data" data-line-start="6" data-line-end="10">
<p class="has-line-data" data-line-start="6" data-line-end="9">Create virtual enviroment<br>
If you do not have virtualenv installed, you can install it with the following command: <code>pip install virtualenv</code><br>
Create virtual enviroment: <code>virtualenv vitual_enviroment_name</code></p>
</li>
<li class="has-line-data" data-line-start="10" data-line-end="14">
<p class="has-line-data" data-line-start="10" data-line-end="13">Activate virtual enviroment<br>
In Linux and Mac: <code>source vitual_enviroment_name/bin/activate</code><br>
In Windows: <code>.\vitual_enviroment_name\Scripts\activate</code></p>
</li>
<li class="has-line-data" data-line-start="14" data-line-end="17">
<p class="has-line-data" data-line-start="14" data-line-end="16">Install dependencies<br>
Run this command: <code>pip install -r requirements.txt</code></p>
</li>
</ol>
<p class="has-line-data" data-line-start="17" data-line-end="18">Run the project</p>
<ol>
<li class="has-line-data" data-line-start="18" data-line-end="22">
<p class="has-line-data" data-line-start="18" data-line-end="21">List all tasks: <code>python python task-cli.py list</code><br>
Output:<br>
<img src="outputs/list.png" alt="alt text"></p>
</li>
<li class="has-line-data" data-line-start="22" data-line-end="28">
<p class="has-line-data" data-line-start="22" data-line-end="27">List by status: <code>python task-cli.py list filter</code><br>
Valid arguments = todo, done, in-progress<br>
Example: <code>python task-cli.py list in-progress</code><br>
Output:<br>
<img src="outputs/list_in_progress.png" alt="alt text"><br>
Example for invalid arguments: <code>python task-cli.py list something</code><br>
Output: 
<img src="outputs/list_something.png" alt="alt text"><br>
Example for the status not found: <code>python task-cli.py list done</code><br>
Output:<br>
<img src="outputs/list_done.png" alt="alt text"><br>
</p>
</li>
<li class="has-line-data" data-line-start="28" data-line-end="31">
<p class="has-line-data" data-line-start="28" data-line-end="30">Add a new task: <code>python task-cli.py add &quot;task&quot;</code><br>
Example: <code>python task-cli.py add &quot;Buy milk and sugar&quot;</code><br>
Output:<br>
<img src="outputs/add.png" alt="alt text"></p>
</li>
<li class="has-line-data" data-line-start="31" data-line-end="35">
<p class="has-line-data" data-line-start="31" data-line-end="34">Delete a task: <code>python task-cli.py delete ID</code><br>
Example: <code>python task-cli.py delete 3</code><br>
Output:<br>
<img src="outputs/delete.png" alt="alt text"><br>
Example for the tasks not found: <code>python task-cli.py delete 9</code><br>
Output:<br>
<img src="outputs/not_found.png" alt="alt text"><br>
</p>
</li>
<li class="has-line-data" data-line-start="35" data-line-end="39">
<p class="has-line-data" data-line-start="35" data-line-end="38">Update a task: <code>python task-cli.py update ID &quot;task&quot;</code><br>
Example: <code>python task-cli.py update 2 &quot;Wash the dishes&quot;</code><br>
Output:<br>
<img src="outputs/update.png" alt="alt text"><br>
Example for the tasks not found: <code>python task-cli.py update 9 &quot;Workout&quot;</code><br>
Output:<br>
<img src="outputs/not_found.png" alt="alt text"><br>
</p>
</li>
<li class="has-line-data" data-line-start="39" data-line-end="43">
<p class="has-line-data" data-line-start="39" data-line-end="42">Mark as in-progress: <code>python task-cli.py mark-in-progress ID</code><br>
Example: <code>python task-cli.py mark-in-progress 3</code><br>
Output:<br>
<img src="outputs/mark_progress.png" alt="alt text"><br>
Example for the tasks not found: <code>python task-cli.py mark-in-progress 9</code><br>
Output:<br>
<img src="outputs/not_found.png" alt="alt text"><br>
</p>
</li>
<li class="has-line-data" data-line-start="43" data-line-end="47">
<p class="has-line-data" data-line-start="43" data-line-end="46">Mark as done: <code>python task-cli.py mark-done ID</code><br>
Example: <code>python task-cli.py mark-done 0</code><br>
Output: Task ID updated successfully!<br>
<img src="outputs/mark_done.png" alt="alt text"><br>
Example for the tasks not found: <code>python task-cli.py mark-done 9</code><br>
Output:<br>
<img src="outputs/not_found.png" alt="alt text"><br>
</p>
</li>
</ol>
<p class="has-line-data" data-line-start="47" data-line-end="48"><a href="https://roadmap.sh/projects/task-tracker">Project Link</a></p>
</body></html>
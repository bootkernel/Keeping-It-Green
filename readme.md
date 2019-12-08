<h1>Keeping It Green</h1>

<p>Keeping It Green is a super simple python script that uses Selenium to help you keep committed to GitHub even when you're sleeping.</p><p>This is a simple documentation on the project to help you get started. </p>

<p><b>Note: </b>The tutorial assumes that you're using a Unix based machine.</p>

<h1>To setup the script</h1>
<p>This script requires the Selenium framework and the <code>chromedriver</code></p>

<h2>In github</h2>
<list>1. Create a dummy repository in Github <br>2. In the repository, create and name the file</list>
<br>
<h2>In your operating system</h2>
<p>
<list>1. Install python 2.7 <br>2. To install selenium, using terminal type,<code> pip install selenium</code><br>3. To download <code>chromedriver</code>, go to: <a>https://sites.google.com/a/chromium.org/chromedriver/downloads</a></list>
</p>
<p><b>Note:</b> If you want to run this script using other browsers, please refer to: <a>https://selenium-python.readthedocs.io/installation.html</a></p>

<h2>In the script</h2>

<p>Changes in the script in terms of functionality is not required however, cutting down steps is encouraged.</p><p>The current logic is set in a loop and the action makes 2 commits,</p>

<list>1. In the repository, delete the current <code>filename</code><br>2. Create another file with the same <code>filename</code><br>3. Exit the browser, repeat <code>Step 1</code></list>





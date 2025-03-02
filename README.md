# Secret Language Encoder and Decoder 
Description:<br>
This Python program allows users to encode and decode secret messages using a simple transformation technique. It adds a layer of obfuscation to your messages, making them unreadable to those who don't know the method.<br>

How it Works:<br>
✅ Encoding:<br>

If a word has 3 or fewer letters, it is simply reversed.<br>
If a word has more than 3 letters, three random letters are added at the start and end, and the first letter moves to the end before encoding.<br>
✅ Decoding:<br>

If the word was reversed, it is simply reversed again.<br>
If the word had extra letters, the random letters are removed, and the last letter is moved back to the beginning to reconstruct the original word.<br>
Key Features:<br>
✔️ Interactive console-based experience<br>
✔️ Automatic retry option for encoding or decoding multiple messagesv
✔️ Randomized encoding for added security<br>
✔️ Easy-to-use interface<br>

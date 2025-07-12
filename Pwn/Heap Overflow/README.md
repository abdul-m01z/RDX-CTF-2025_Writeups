## <h1>Heap Overflow</h1>

**Note**: This is an unofficial writeup by [@KekeSenpai23](https://github.com/KekeSenpai23), the team who came 1st in the ctf

## Writeup

This challenge was a heap challenge (as expected from the name). So, first of all I analyzed the binary in IDA to see the source code as it wasn't provided with the challenge. Upon Analysing the binary I found that the pointer of the allocated chunk gets xored with a global key.
<br>
<img width="850" height="211" alt="Image" src="https://github.com/user-attachments/assets/32e2d637-0770-48a0-8e61-711d492c721c" />
<br>
Also, upon analyzing the edit_arena() function I found out that the program is vulnerable to heap overflow letting us overwrite the pointer of the allocation in the end.
<br><img width="367" height="150" alt="Image" src="https://github.com/user-attachments/assets/788ea36c-6a1e-463a-86c2-7942a60a7cb0" />
<br>So, I tried analysing the binary in GDB (I use pwndbg). I found the offset to be at 0x40 and after 0x40 our input will overwrite the pointer.
<br><img width="866" height="197" alt="Image" src="https://github.com/user-attachments/assets/5ac263d3-539e-4f4b-b940-e517761345e2" />
<br>Now, I try overflowing the pointer.
<br><img width="735" height="71" alt="Image" src="https://github.com/user-attachments/assets/e2ad71f0-91d0-4569-b6dd-ec85d7963797" />
<br>As you can see, we overflowed the ptr and it caused the program to crash as the address is invalid... but the hex value overflowing the address isnt anything like the cyclic pattern we generated and sent. Now, considering the global key we discussed about before, We know that our input from 0x40 till 0x48 is being xored with a global key which we yet don't know what is. So, lets find the global key.
<br><img width="502" height="52" alt="Image" src="https://github.com/user-attachments/assets/596c1d7b-6fbb-497c-9d93-0cd7c0ced1eb" />
<br>Easy enough... Well, now we have the global key, PIE is disabled and we can overflow in HEAP and get RIP control. So now we just need to figure out what to xor with. Also to trigger the secret and key code lines we need to first give a pointer. So, lets put in win_arena address and xor it with the global key to test it out.
<br><img width="489" height="209" alt="Image" src="https://github.com/user-attachments/assets/3d6fd714-396e-4205-a6c0-4b87a4d102ec" />
<br>This gave me this address:
<br><img width="388" height="58" alt="Image" src="https://github.com/user-attachments/assets/1939246b-ef27-42a3-a037-101451b4462d" />
<br>This is where I got creative... I thought "Hey, if xoring global key and win gives me this address won't xoring this address with the global key give me win function?". And sure enough, It worked.
<br><img width="719" height="91" alt="Image" src="https://github.com/user-attachments/assets/38881e16-279a-4ae7-82e4-34cc88a74bf1" />
<br>And we also needed the correct secret and key which can be found in the decompilation:
<br><img width="396" height="32" alt="Image" src="https://github.com/user-attachments/assets/2d5e2dbf-25ea-4c9d-86de-2882aed3d585" />
<br>Through all of this I wrote the exploit and ETVIOLA! I got the flag!
<br><img width="471" height="118" alt="Image" src="https://github.com/user-attachments/assets/f06508eb-a6c9-4efa-851d-78534a3210aa" />
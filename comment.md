In your book, under the section "Setting Up A Vector Database", you write:

> Model configuration: Choose `text-embedding-3-small`, the OpenAI
> embedding model we'll use; the value of dimensions should automatically
> be set to 1536.

When I created my Pinecone index, the dimensions were set to 512. I did not see the dropdown box that sets dimensions, so I struggled a bit. You can set it on the same screen where you name the index.

After you select your model under "Configuration", you see:

```
Index configured for text-embedding-3-small
Modality:    Text
Vector type: Dense
Max input:   8192
Dimension:   512
Metric:      Cosine
```

The "Dimension" has a dropdown box. You set the dimension there. Once that's done, your code works fine.

const ENC_STRING = ""

async function decrypt (PASSWORD) {
  let raw = atob(ENC_STRING)
  const C = new Uint8Array(new ArrayBuffer(raw.length))
  for (let i = 0; i < raw.length; i++) C[i] = raw.charCodeAt(i)

  return new TextDecoder().decode(
    await crypto.subtle.decrypt(
      {
        name: 'AES-CBC',
        iv: C.slice(0, 16)
      },
      await crypto.subtle.deriveKey(
        {
          name: 'PBKDF2',
          salt: C.slice(0, 16),
          iterations: 100000,
          hash: 'SHA-256'
        },
        await crypto.subtle.importKey(
          'raw',
          new TextEncoder().encode(PASSWORD),
          'PBKDF2',
          false,
          ['deriveKey']
        ),
        { name: 'AES-CBC', length: 256 },
        false,
        ['decrypt']
      ),
      C.slice(16)
    )
  )
}

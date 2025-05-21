import { useState } from 'react'
import axios from 'axios'

export default function IndexingPage() {
  const [filePath, setFilePath] = useState('')
  const [message, setMessage] = useState('')

  const handleIndex = async () => {
    try {
      const res = await axios.post('/api/v1/index/', {
        file_path: filePath,
        batch: false
      })
      setMessage(res.data.message)
    } catch (err: any) {
      setMessage(err.response?.data?.detail || 'Error')
    }
  }

  return (
    <main className="min-h-screen p-8 bg-white text-black font-brutal">
      <h1 className="text-3xl mb-4">Indicizzazione</h1>
      <div className="space-y-4">
        <input
          type="text"
          placeholder="Percorso file o cartella"
          value={filePath}
          onChange={e => setFilePath(e.target.value)}
          className="border-4 border-black p-2 w-full"
        />
        <button
          onClick={handleIndex}
          className="border-4 border-black px-4 py-2 hover:bg-black hover:text-white"
        >
          Avvia Indicizzazione
        </button>
        {message && <p className="mt-4">{message}</p>}
      </div>
    </main>
  )
}

import { useState } from 'react'
import axios from 'axios'

type Chunk = {
  id: string
  content: string
  metadata: string
}

export default function RetrievalPage() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<Chunk[]>([])
  const [error, setError] = useState('')

  const handleRetrieve = async () => {
    try {
      const res = await axios.post('/api/v1/retrieve/', {
        query,
        top_k: 5,
        filters: null
      })
      setResults(res.data)
      setError('')
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Error')
    }
  }

  return (
    <main className="min-h-screen p-8 bg-white text-black font-brutal">
      <h1 className="text-3xl mb-4">Recupero</h1>
      <div className="mb-4">
        <input
          type="text"
          placeholder="Termini di ricerca"
          value={query}
          onChange={e => setQuery(e.target.value)}
          className="border-4 border-black p-2 w-full"
        />
      </div>
      <button
        onClick={handleRetrieve}
        className="border-4 border-black px-4 py-2 hover:bg-black hover:text-white mb-6"
      >
        Recupera Chunk
      </button>
      {error && <p className="text-red-600">{error}</p>}
      <ul className="space-y-4">
        {results.map(chunk => (
          <li key={chunk.id} className="border-2 border-black p-4">
            <p className="font-bold">{chunk.id}</p>
            <p>{chunk.content}</p>
            <p className="italic text-sm">{chunk.metadata}</p>
          </li>
        ))}
      </ul>
    </main>
  )
}

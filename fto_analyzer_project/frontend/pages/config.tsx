import { useState } from 'react'
import axios from 'axios'

export default function ConfigPage() {
  const [weaviateUrl, setWeaviateUrl] = useState('')
  const [weaviateKey, setWeaviateKey] = useState('')
  const [message, setMessage] = useState('')

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      const res = await axios.post('/api/v1/config/', {
        weaviate_url: weaviateUrl,
        weaviate_api_key: weaviateKey
      })
      setMessage(res.data.message)
    } catch (err: any) {
      setMessage(err.response?.data?.detail || 'Error')
    }
  }

  return (
    <main className="min-h-screen p-8 bg-white text-black font-brutal">
      <h1 className="text-3xl mb-4">Configurazione</h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block mb-1">Weaviate URL</label>
          <input
            type="text"
            value={weaviateUrl}
            onChange={e => setWeaviateUrl(e.target.value)}
            className="border-4 border-black p-2 w-full"
          />
        </div>
        <div>
          <label className="block mb-1">Weaviate API Key</label>
          <input
            type="text"
            value={weaviateKey}
            onChange={e => setWeaviateKey(e.target.value)}
            className="border-4 border-black p-2 w-full"
          />
        </div>
        <button type="submit" className="border-4 border-black px-4 py-2 hover:bg-black hover:text-white">
          Salva Configurazione
        </button>
      </form>
      {message && <p className="mt-4">{message}</p>}
    </main>
  )
}

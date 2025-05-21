import { useState } from 'react'
import axios from 'axios'

export default function AnalysisPage() {
  const [claim, setClaim] = useState('')
  const [description, setDescription] = useState('')
  const [result, setResult] = useState<{
    decomposition: string
    risks: string
    design_around: string
    technical_rationale: string
  } | null>(null)
  const [error, setError] = useState('')

  const handleAnalyze = async () => {
    try {
      const res = await axios.post('/api/v1/analyze/', {
        third_party_claim: claim,
        user_description: description,
        top_k: 5
      })
      setResult(res.data)
      setError('')
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Error')
    }
  }

  return (
    <main className="min-h-screen p-8 bg-white text-black font-brutal">
      <h1 className="text-3xl mb-4">Analisi FTO</h1>
      <div className="space-y-4 mb-4">
        <textarea
          placeholder="Testo del claim di terzi"
          value={claim}
          onChange={e => setClaim(e.target.value)}
          className="w-full border-4 border-black p-2 h-24"
        />
        <textarea
          placeholder="Descrizione del tuo prodotto/processo"
          value={description}
          onChange={e => setDescription(e.target.value)}
          className="w-full border-4 border-black p-2 h-24"
        />
        <button
          onClick={handleAnalyze}
          className="border-4 border-black px-4 py-2 hover:bg-black hover:text-white"
        >
          Avvia Analisi
        </button>
      </div>
      {error && <p className="text-red-600">{error}</p>}
      {result && (
        <section className="space-y-4">
          <div>
            <h2 className="font-bold">Decomposizione</h2>
            <p>{result.decomposition}</p>
          </div>
          <div>
            <h2 className="font-bold">Rischi</h2>
            <p>{result.risks}</p>
          </div>
          <div>
            <h2 className="font-bold">Design Around</h2>
            <p>{result.design_around}</p>
          </div>
          <div>
            <h2 className="font-bold">Motivazioni Tecniche</h2>
            <p>{result.technical_rationale}</p>
          </div>
        </section>
      )}
    </main>
  )
}

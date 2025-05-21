import Link from 'next/link'

export default function Home() {
  return (
    <main className="min-h-screen bg-white text-black font-brutal p-8">
      <h1 className="text-4xl mb-6">FTO Analyzer</h1>
      <nav className="space-y-4">
        <Link href="/config" className="inline-block border-4 border-black px-4 py-2 hover:bg-black hover:text-white">
            Configurazione
        </Link>
        <Link href="/indexing" className="inline-block border-4 border-black px-4 py-2 hover:bg-black hover:text-white">
            Indicizzazione
        </Link>
        <Link href="/retrieval" className="inline-block border-4 border-black px-4 py-2 hover:bg-black hover:text-white">
            Recupero
        </Link>
        <Link href="/analysis" className="inline-block border-4 border-black px-4 py-2 hover:bg-black hover:text-white">
            Analisi FTO
        </Link>
      </nav>
    </main>
  )
}

import Link from 'next/link'

export default function Home() {
  return (
    <main className="min-h-screen bg-white text-black font-brutal p-8">
      <h1 className="text-4xl mb-6">FTO Analyzer</h1>
      <nav className="space-y-4">
        <Link href="/config">
          <a className="inline-block border-4 border-black px-4 py-2 hover:bg-black hover:text-white">
            Configurazione
          </a>
        </Link>
        <Link href="/indexing">
          <a className="inline-block border-4 border-black px-4 py-2 hover:bg-black hover:text-white">
            Indicizzazione
          </a>
        </Link>
        <Link href="/retrieval">
          <a className="inline-block border-4 border-black px-4 py-2 hover:bg-black hover:text-white">
            Recupero
          </a>
        </Link>
        <Link href="/analysis">
          <a className="inline-block border-4 border-black px-4 py-2 hover:bg-black hover:text-white">
            Analisi FTO
          </a>
        </Link>
      </nav>
    </main>
  )
}

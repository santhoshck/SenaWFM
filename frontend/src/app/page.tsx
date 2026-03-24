import Link from 'next/link';

export default function Home() {
  return (
    <div className="min-h-screen bg-white dark:bg-gray-900 flex flex-col items-center justify-center relative overflow-hidden">
      {/* Decorative background gradients */}
      <div className="absolute inset-0 z-0 overflow-hidden pointer-events-none">
        <div className="absolute top-[10%] left-[10%] w-[40%] h-[40%] rounded-full bg-gradient-to-br from-blue-100/40 to-indigo-100/40 dark:from-blue-900/20 dark:to-indigo-900/20 blur-3xl opacity-60"></div>
        <div className="absolute bottom-[10%] right-[10%] w-[50%] h-[50%] rounded-full bg-gradient-to-bl from-purple-100/40 to-pink-100/40 dark:from-purple-900/20 dark:to-pink-900/20 blur-3xl opacity-60"></div>
      </div>

      <main className="flex flex-col items-center justify-center flex-1 w-full px-6 sm:px-20 text-center relative z-10">
        <div className="inline-flex items-center justify-center px-4 py-1.5 mb-8 text-sm font-medium text-blue-600 bg-blue-50 dark:bg-blue-900/30 dark:text-blue-300 rounded-full ring-1 ring-inset ring-blue-500/20 dark:ring-blue-400/20">
          Welcome to the Future of WFM
        </div>
        
        <h1 className="text-5xl sm:text-7xl font-extrabold tracking-tight text-gray-900 dark:text-white mb-6">
          Sena<span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600 dark:from-blue-400 dark:to-indigo-400">WFM</span>
        </h1>
        
        <p className="max-w-2xl text-xl sm:text-2xl text-gray-600 dark:text-gray-300 mb-12 leading-relaxed">
          The all-in-one platform for managing your workforce, optimizing schedules, and driving team success.
        </p>
        
        <div className="flex flex-col sm:flex-row items-center gap-4 w-full sm:w-auto">
          <Link
            href="/login"
            className="w-full sm:w-auto px-8 py-4 text-lg font-medium text-white transition-all duration-200 bg-gradient-to-r from-blue-600 to-indigo-600 rounded-xl hover:from-blue-700 hover:to-indigo-700 hover:shadow-lg hover:-translate-y-0.5 active:translate-y-0 active:shadow-md focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          >
            Access Dashboard &rarr;
          </Link>
          <a
            href="https://github.com"
            target="_blank"
            rel="noopener noreferrer"
            className="w-full sm:w-auto px-8 py-4 text-lg font-medium text-gray-700 dark:text-gray-200 transition-all duration-200 bg-white dark:bg-gray-800 border-2 border-gray-200 dark:border-gray-700 rounded-xl hover:border-gray-300 dark:hover:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-200"
          >
            Learn More
          </a>
        </div>
      </main>
    </div>
  );
}

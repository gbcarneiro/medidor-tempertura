"use client";
import Image from 'next/image'
import Button from '../components/Button'

import { useState } from 'react';

export default function Home() {
  const [temp, setTemp] = useState(0.0);
  const [data, setData] = useState('');
  const [horario, setHorario] = useState('');
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm lg:flex">
        <p className="fixed left-0 top-0 flex w-full justify-center border-b border-gray-300 bg-gradient-to-b from-zinc-200 pb-6 pt-8 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:static lg:w-auto  lg:rounded-xl lg:border lg:bg-gray-200 lg:p-4 lg:dark:bg-zinc-800/30">
          Temperatura medida em: {data} às {horario}
        </p>
      </div>

      <div>
        <Image
          className=""
          src="/temperature.png"
          alt="Logo temperatura"
          width={100}
          height={100}
          priority
        />
        <h1>{temp}º C</h1>
      </div>

      <div className="">
        <Button
          onClick={async () => {
            try {
              const response = await fetch(
                'https://flask-hello-world-eight-black.vercel.app/get/temperature',
                { method: 'GET', cache: 'no-cache' }
              );
              const responseData = await response.json();

              setTemp(responseData.temperature);
              setData(responseData.date); // Adjust this based on your API response
              setHorario(responseData.hour); // Adjust this based on your API response
              console.log(responseData);
            } catch (error) {
              console.error('Error fetching temperature:', error);
            }
          }}
        >
          Atualizar temperatura
        </Button>
      </div>
    </main>
  )
}

 'use client'
//import Image from "next/image";
import { useState } from 'react';
import { useFuzzySearchList, Highlight } from '@nozbe/microfuzz/react'
import { FuzzySearchStrategy , FuzzyResult, HighlightRanges} from '@nozbe/microfuzz'
import { data } from './data.json'
type Source = typeof data extends (infer U)[] ? U : never;
type FSResult = FuzzyResult<Source>
const mapResultItem = ({ item, matches: [highlightRanges] }: FSResult): [s:Source,h: HighlightRanges| null] => [item, highlightRanges]
const getItemText = (item: Source) => [`${item.name} ${item.category}`]
export default function Search() {
  const [queryText, setQueryText] = useState('')
  // const [strategy, setStrategy] = useState<FuzzySearchStrategy>('smart')
  const strategy: FuzzySearchStrategy = 'smart'
  const filtered = useFuzzySearchList({ list: data, queryText, mapResultItem, strategy, getText:getItemText })
   const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setQueryText(event.target.value); // 3. Update the state
  };
  return (
    <>
        <div className="rounded-md p-[3px] bg-gradient-to-r from-banner-start to-banner-end focus-within:motion-safe:animate-bg-loop bg-[length:120%_120%]">
          <input className="w-80 bg-gray-900 p-2 rounded-md focus:outline-none" placeholder="" onChange={handleInputChange} />
        </div>
<ul className="lg:w-[70%] xl:w-[50%] flex flex-col gap-8">
         {/* TODO: showing x amount filter */}
        {filtered.slice(0, 100).map(([item,hg ]) => (
          <li className='flex flex-col bg-black/60 w-full p-8 min-h-40 rounded-lg border  border-white' key={item.name}>
            {/*<Highlight text={item.name} ranges={highlightRanges} />*/}
               <h4 className='text-xl font-black'><Highlight text={item.name} ranges={hg}/></h4>
               <p className=''>{item.description}</p>
               <div className='flex flex-row gap-4 mt-10 '>
               {item.tags.map((t) => 
                 <span key={`${item.name}-${t}`} className='text-xs w-fit text-black rounded-full bg-yellow-400 px-2 '>{t}</span>
               )}
               </div>
          </li>
        ))}
      </ul>
        </>
       );
}

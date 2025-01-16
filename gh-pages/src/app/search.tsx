 'use client'
import Image from "next/image";
import { useState } from 'react';
import { useFuzzySearchList, Highlight } from '@nozbe/microfuzz/react'
import { FuzzySearchStrategy , FuzzyResult, HighlightRanges} from '@nozbe/microfuzz'
import { data } from './data.json'
type Source = typeof data extends (infer U)[] ? U : never;
type FSResult = FuzzyResult<Source>
const mapResultItem = ({ item, matches: [highlightRanges] }: FSResult): [s:Source,h: HighlightRanges| null] => [item, highlightRanges]
export default function Search() {
  const [queryText, setQueryText] = useState('')
  const [strategy, setStrategy] = useState<FuzzySearchStrategy>('smart')
  const filtered = useFuzzySearchList({ list: data, queryText, mapResultItem, strategy })
   const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setQueryText(event.target.value); // 3. Update the state
  };
  return (
    <>
        <div className="rounded-md p-[3px] bg-gradient-to-r from-banner-start to-banner-end focus-within:motion-safe:animate-bg-loop bg-[length:120%_120%]">
          <input className="w-80 bg-gray-900 p-2 rounded-md focus:outline-none" placeholder="read input | xargs find -type l " onChange={handleInputChange} />
        </div>
<ul className="results">
        {filtered.slice(0, 40).map(([item, highlightRanges]) => (
          <li key={item.name}>
            <Highlight text={item.name} ranges={highlightRanges} />
          </li>
        ))}
      </ul>
        </>
       );
}

import React, { useState } from 'react'; import { Card, CardContent } from '@/components/ui/card'; import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from '@/components/ui/select'; import { Button } from '@/components/ui/button';

const options = { health: ['Low', 'High'], cps: ['Low', 'High'], gamesense: ['Low', 'Medium', 'High'], pearl: ['Short', 'Medium', 'Long'], web: ['Used', 'Not Used'], gap: ['Short Gap', 'None'], totem: ['Used', 'Not Used'], playstyle: ['Aggro', 'Balanced', 'Defensive'], };

const evaluateMatchup = (a, b) => { // Example rule: Defensive beats Aggro if (a.playstyle === 'Defensive' && b.playstyle === 'Aggro') return 'Player A Wins'; if (b.playstyle === 'Defensive' && a.playstyle === 'Aggro') return 'Player B Wins'; if (a.playstyle === 'Aggro' && b.playstyle === 'Balanced') return 'Player A Wins'; if (b.playstyle === 'Aggro' && a.playstyle === 'Balanced') return 'Player B Wins'; if (a.playstyle === 'Balanced' && b.playstyle === 'Defensive') return 'Player A Wins'; if (b.playstyle === 'Balanced' && a.playstyle === 'Defensive') return 'Player B Wins';

// CPS vs CPS if (a.cps === 'High' && b.cps === 'Low' && a.gamesense !== 'Low') return 'Player A Wins'; if (b.cps === 'High' && a.cps === 'Low' && b.gamesense !== 'Low') return 'Player B Wins';

// Default rule return 'Tie'; };

export default function PvPStrategySimulator() { const [playerA, setPlayerA] = useState({}); const [playerB, setPlayerB] = useState({}); const [result, setResult] = useState('');

const handleCompare = () => { setResult(evaluateMatchup(playerA, playerB)); };

const handleChange = (player, key, value) => { if (player === 'A') setPlayerA(prev => ({ ...prev, [key]: value })); else setPlayerB(prev => ({ ...prev, [key]: value })); };

return ( <div className="grid grid-cols-2 gap-4 p-4"> {[['A', playerA], ['B', playerB]].map(([label, player]) => ( <Card key={label}> <CardContent className="space-y-2"> <h2 className="text-xl font-bold">Player {label}</h2> {Object.entries(options).map(([key, values]) => ( <Select key={key} onValueChange={val => handleChange(label, key, val)}> <SelectTrigger> <SelectValue placeholder={${key.charAt(0).toUpperCase() + key.slice(1)}} /> </SelectTrigger> <SelectContent> {values.map(option => ( <SelectItem key={option} value={option}>{option}</SelectItem> ))} </SelectContent> </Select> ))} </CardContent> </Card> ))} <div className="col-span-2 flex flex-col items-center"> <Button onClick={handleCompare}>Compare Strategies</Button> {result && <div className="mt-4 text-xl font-bold">Result: {result}</div>} </div> </div> ); }


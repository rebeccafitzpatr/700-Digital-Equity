import React from 'react';

export default function ListItem({ record }){
  return (
    <li>
      <p>Name: {record.name}</p>
      <p>Score: {record.score}</p>
    </li>
  );
};

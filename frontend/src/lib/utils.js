export const CATEGORIES = ['All', 'Technology', 'Science', 'Finance', 'Health', 'Travel', 'Business', 'AI', 'General'];

export function imageFor(post) {
  const content = post?.content ?? '';
  // Priority 1: Manual [Image: url] tag
  // Priority 2: Any raw image URL in text
  const match = content.match(/\[Image:\s*(https?:\/\/[^\]\s]+)\]/i) || content.match(/https?:\/\/[^\s)]+\.(?:png|jpe?g|gif|webp)/i);
  if (match) return match[1] ?? match[0];

  const cat = (post?.category ?? 'General').toLowerCase();
  const map = {
    technology: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=900&q=80',
    science: 'https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&w=900&q=80',
    finance: 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=900&q=80',
    health: 'https://images.unsplash.com/photo-1505751172876-fa1923c5c528?auto=format&fit=crop&w=900&q=80',
    travel: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=900&q=80',
    business: 'https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=900&q=80',
    ai: 'https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=900&q=80',
    general: 'https://images.unsplash.com/photo-1499750310107-5fef28a66643?auto=format&fit=crop&w=900&q=80'
  };
  return map[cat] ?? map.general;
}

/**
 * Removes image tags so they don't show up in post previews
 */
export function cleanContent(content = '') {
  return content.replace(/\[Image:\s*https?:\/\/[^\]]+\]/gi, '').trim();
}

/**
 * Simple text truncation for card descriptions
 */
export function truncate(text = '', length = 100) {
  if (text.length <= length) return text;
  return text.slice(0, length).trim() + '...';
}

export function formatDate(iso) {
  if (!iso) return 'Recently';
  const date = new Date(iso);
  // Check for invalid dates
  if (isNaN(date.getTime())) return 'Recently';
  return date.toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' });
}

export function readTime(text = '') {
  // Filter out image tags from read time calculation
  const cleanText = cleanContent(text);
  const words = cleanText.trim().split(/\s+/).filter(Boolean).length;
  const minutes = Math.max(1, Math.ceil(words / 200)); // 200 wpm is standard
  return `${minutes} min read`;
}

export function getSavedSet(key, userId = 'guest') {
  if (typeof window === 'undefined') return new Set(); // SSR safety
  try { 
    return new Set(JSON.parse(localStorage.getItem(`${key}_${userId}`) ?? '[]')); 
  } catch { 
    return new Set(); 
  }
}

export function toggleSaved(key, postId, userId = 'guest') {
  const set = getSavedSet(key, userId);
  const id = String(postId);
  if (set.has(id)) set.delete(id); else set.add(id);
  localStorage.setItem(`${key}_${userId}`, JSON.stringify([...set]));
  return set.has(id);
}

/**
 * Fisher-Yates Shuffle for randomized "Recommended" feeds
 */
export function shuffle(arr) {
  const newArr = [...arr];
  for (let i = newArr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [newArr[i], newArr[j]] = [newArr[j], newArr[i]];
  }
  return newArr;
}
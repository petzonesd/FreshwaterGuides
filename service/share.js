/* Share-link encoding for the service toolkit. The payload lives in the URL fragment (#), which browsers never send to a server. */
(function (root) {
  'use strict';
  function b64u(u8) { var s = ''; for (var i = 0; i < u8.length; i++) s += String.fromCharCode(u8[i]); return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, ''); }
  function unb64u(str) {
    str = str.replace(/-/g, '+').replace(/_/g, '/'); while (str.length % 4) str += '=';
    var bin = atob(str), u8 = new Uint8Array(bin.length); for (var i = 0; i < bin.length; i++) u8[i] = bin.charCodeAt(i); return u8;
  }
  async function pipe(u8, Stream, fmt) {
    var s = new Stream(fmt), w = s.writable.getWriter(); w.write(u8); w.close();
    return new Uint8Array(await new Response(s.readable).arrayBuffer());
  }
  async function encode(obj) {
    var bytes = new TextEncoder().encode(JSON.stringify(obj));
    if (root.CompressionStream) return 'z.' + b64u(await pipe(bytes, root.CompressionStream, 'deflate-raw'));
    return 'p.' + b64u(bytes);
  }
  async function decode(token) {
    var kind = token.slice(0, 2), u8 = unb64u(token.slice(2));
    if (kind === 'z.') u8 = await pipe(u8, root.DecompressionStream, 'deflate-raw');
    return JSON.parse(new TextDecoder().decode(u8));
  }
  async function link(obj) { return location.origin + '/service/view/#' + await encode(obj); }
  root.FWGShare = { encode: encode, decode: decode, link: link };
})(window);

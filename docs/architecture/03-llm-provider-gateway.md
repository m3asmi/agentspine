# LLM Provider Gateway

## Goal

Provide a provider-agnostic model access layer so the framework can:

- use Ollama by default
- switch to an OpenAI-compatible provider without rewriting orchestration code
- compare outputs across providers
- log model/provider usage consistently

## Why this exists

The framework must not let graph nodes or plugins call provider SDKs directly.

Without a gateway:

- provider logic leaks into workflows
- fallback logic becomes inconsistent
- audit quality drops
- cost and latency comparison becomes harder

## Responsibilities

- provider profile management
- routing mode selection
- compatibility matrix enforcement
- local/remote fallback behavior
- compare mode support
- LLM audit event emission

## Supported provider kinds

- ollama_openai_compat
- openai_compat
- openai_native

## Required routing modes

- local_only
- remote_only
- manual_compare
- fallback_on_failure
- fallback_on_low_confidence

## Required provider fields

- provider_id
- provider_kind
- base_url
- api_key
- model
- timeout
- max_retries
- supports_tools
- supports_vision
- supports_audio_in
- supports_embeddings
- supports_responses_api
- supports_streaming
- cost_class
- reliability_class

## Logging requirements

Each call must log:

- provider_id
- model
- routing_mode
- fallback_reason
- latency
- token usage if available
- input hash
- output hash
- compare score if used

